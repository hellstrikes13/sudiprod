mport boto3
import sys
# Author: Sudeep Melekar <sudeep@helpshift.com>
# Purpose: Create/Modify rule in ALB for blocking spammer IP for scopely domain

def check_duplicates():
  ''' Check if entered IP is already present in the scopely"s ALB rule'''
  if src_ip in total_ips:
    print('The IP',src_ip,'is found in ALB rule and cannot add duplicates, exiting the script Good Bye sleep well !')
    sys.exit(2)

def modify_rule():
  ''' Modify ALB rule to add the new source IP list '''
  #NOTE: ALB has limitation of adding 3 IPs in source IP list condition for every rule
  for rl in total_rules:
    scopely_modify_arn = rl['RuleArn']
    if len([ i['SourceIpConfig']['Values'] for i in rl['Conditions'] if i['Field'] == 'source-ip'].pop()) < 3:
      src_ip_lst.append(src_ip)
      modify_condition = [
      {
          'Field': 'source-ip',
          'SourceIpConfig': {
               'Values': src_ip_lst
          },
      },
      {
          'Field': 'path-pattern',
          'PathPatternConfig': {
               'Values': [
                  '/websdk/scopely/*',
            ]
           },
      },
      {
          'Field': 'host-header',
          'HostHeaderConfig': {
              'Values': [
                 'api.helpshift.com'
            ],
           },
       },
      ]
      resp = client.modify_rule(
         RuleArn=scopely_modify_arn,
         Conditions=modify_condition
      )
      print('---Rule modified successfully---')
      sys.exit(0)
    else:
      pass

def create_rule():
  ''' Create new rule & add source IP if there are already 3 IPs present in  the sourceIP list for current alb rule'''
  last_rule_priority=int(''.join(pri_lst[-1:]))
  for rul in total_rules:
    scopely_create_arn = rul['RuleArn']
    current_priority = int(rul['Priority'])
    if len(src_ip_lst) == 3 and current_priority == last_rule_priority:
      new_condition = [
      {
          'Field': 'source-ip',
          'SourceIpConfig': {
             'Values': [src_ip],
          },
      },
      {
          'Field': 'path-pattern',
          'PathPatternConfig': {
             'Values': [
                '/websdk/scopely/*',
            ]
           },
      },
      {
          'Field': 'host-header',
          'HostHeaderConfig': {
             'Values': [
                'api.helpshift.com'
            ],
           },
       },
      ]
      fixed_response_action = {
      'Type': 'fixed-response',
      'FixedResponseConfig': {
          'StatusCode': '200',
          'ContentType': 'text/plain',
          'MessageBody': '200 OK'
        }
      }
      respo = client.create_rule(
         ListenerArn=albarn,
         Conditions=new_condition,
         Priority=last_rule_priority+1,
         Actions=[fixed_response_action]
      )
      print('---Rule created successfully---')
      sys.exit(1)
    else:
      pass

def main():
  global albarn
  global client
  global src_ip
  global src_ip_lst
  global total_ips
  global total_rules
  global pri_lst
  albarn='<YOUR AMAZON RESOURCE NAME>
  src_ip=sys.argv[1]+'/32'
  total_ips = []
  pri_lst=[]
  total_rules = []
  client = boto3.client('elbv2')
  response = client.describe_rules(
    ListenerArn=albarn,
    PageSize=123
  )
  for rule in response['Rules']:
    for condition in rule['Conditions']:
      if 'PathPatternConfig' in condition and condition['PathPatternConfig']['Values'] == ['<specific path to match>/*']:
        src_ip_lst = [ i['SourceIpConfig']['Values'] for i in rule['Conditions'] if i['Field'] == 'source-ip'].pop()
        total_rules.append(rule)
        pri_lst.append(rule['Priority'])
        for i in src_ip_lst: total_ips.append(i)
  check_duplicates()
  modify_rule()
  create_rule()

if __name__ == '__main__':
  main()

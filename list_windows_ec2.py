import boto.ec2
import gevent
global con
def list_win(con):
  ec2res = con.get_all_reservations()
  ec2wins = []
  for k in ec2res:
      if k.instances[0].platform == 'windows':
          ec2wins.append(k.instances[0])
  for j in ec2wins:
      print j.region,',',j.platform,',',j.private_ip_address,',',j.state,',',j.tags['Name'],',',j.tags['Owner']
  ec2wins = []

def con_nv():
  con = boto.ec2.connect_to_region('us-east-1')
  print 'AWS North Virginia: ',con.region
  gevent.sleep(0)
  list_win(con)

def con_org():
  con = boto.ec2.connect_to_region('us-west-2')
  print 'AWS Orgegon: ',con.region
  gevent.sleep(0)
  list_win(con)

def con_ncal():
  con = boto.ec2.connect_to_region('us-west-1')
  print 'AWS North California: ',con.region
  gevent.sleep(0)
  list_win(con)


gevent.joinall([
    gevent.spawn(con_nv),
    gevent.spawn(con_org),
    gevent.spawn(con_ncal)])

pktstream.window(self.window_length, self.sliding_interval).transform(lambda rdd: (rdd.filter(lambda p : (p[1]==str('10032'))).map(lambda p : (p[2:])).map(lambda ((ipv4_dstIP,count1,count2,dns_an_rdata)): ((ipv4_dstIP,dns_an_rdata))).map(lambda ((ipv4_dstIP,dns_an_rdata)): ((i,p,v,4,_,d,s,t,I,P))))).foreachRDD(lambda rdd:send_reduction_keys(rdd, (u'localhost', 4949),0,'10032'))
pktstream.window(self.window_length, self.sliding_interval).transform(lambda rdd: (rdd.filter(lambda p : (p[1]==str('20008'))).map(lambda p : (p[2:])).map(lambda ((ipv4_dstIP,count)): ((ipv4_dstIP),(count))).reduceByKey(lambda x,y: x+y))).foreachRDD(lambda rdd:send_reduction_keys(rdd, (u'localhost', 4949),0,'20008'))
pktstream.window(self.window_length, self.sliding_interval).transform(lambda rdd: (rdd.filter(lambda p : (p[1]==str('20032'))).map(lambda p : (p[2:])).map(lambda ((ipv4_dstIP,count)): ((ipv4_dstIP),(count))).reduceByKey(lambda x,y: x+y))).foreachRDD(lambda rdd:send_reduction_keys(rdd, (u'localhost', 4949),0,'20032'))
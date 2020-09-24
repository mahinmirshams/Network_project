import  dns.resolver

answers = dns.resolver.query('mail.google.com', 'CNAME')
print (' query qname:', answers.qname, ' num ans.', len(answers))
for rdata in answers:
    print (' cname target address:', rdata.target)
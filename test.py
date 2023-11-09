test_str = '''<h3>Can I install Debian on Windows?</h3>
<p style="text-align: justify;"><strong>YES</strong>, you can install Debian by <strong>replacing Windows</strong> or run Debian alongside Windows by <strong>dual boot</strong>. The process comprises <strong>three fundamental steps</strong>. These include <strong>downloading a Debian ISO file, </strong>making a <strong>bootable device with the ISO file</strong>, and finally, proceeding to<strong> install Debian.</strong></p>

<h3>Is Debian free to use?</h3>
<p style="text-align: justify;"><strong>YES</strong>, Debian is free to use. It is a <strong>free and open-source</strong> operating system, and it is released under the <strong>GNU</strong> <strong>General Public License (GPL)</strong>. This means that you are free to use, modify, distribute, and share Debian with others without cost. You can download and install Debian <strong>without any licensing fees</strong>, and you can modify the source code, redistribute it, and contribute to the Debian project if you wish.</p>

<h3>What is Debian Bookworm?</h3>
<p style="text-align: justify;">Debian Bookworm is the <strong>development codename for Debian 12</strong>, a major release of the Debian operating system. Debian is known for using code names based on characters from the 'Toy Story' movies for its development branches. However, as a development codename, 'Bookworm' represents the <strong>unstable branch of Debian</strong>, where new packages and updates are introduced for <strong>testing and development.</strong></p>

<h3>Is Debian better than Ubuntu?</h3>
<p style="text-align: justify;">Both Debian and Ubuntu are popular Linux distributions, and they have their own strengths and characteristics. If you value <strong>long-term stability</strong>, are comfortable with a <strong>less frequent release cycle</strong>, and have <strong>expertise in Linux,</strong> <strong>Debian </strong>might be a better choice. On the other hand, if you prefer <strong>quicker access to the latest software</strong>, or if you're <strong>new to Linux</strong>, <strong>Ubuntu </strong>may be a better fit. Indeed, it's worth noting that Ubuntu is based on Debian, so they share many similarities.</p>

<h3>Which is faster Debian or Kali?</h3>
<p style="text-align: justify;">The speed or performance of a Linux distribution like Debian or Kali Linux depends on various factors, including your <strong>hardware</strong>, the <strong>desktop environment</strong> or window manager you're using, and <strong>how you configure</strong> and use the distribution. Comparing, the speed of Debian and Kali Linux is fundamentally <strong>similar at their core</strong>.</p>'''
quesub1 = "<h3>"
quesub2 = "</h3>"
ansub1 = '<p style="text-align: justify;">'
ansub2 = '</p>'
find = 1
ques = []
ans = []
# getting index of substrings
while(find):
    qidx1 = test_str.find(quesub1)
    qidx2 = test_str.find(quesub2)
    ridx1 = test_str.find(ansub1)
    ridx2 = test_str.find(ansub2)
    if(qidx1==-1 and qidx2==-1):
        find = 0
    else:
        quesres = test_str[qidx1 + len(quesub1): qidx2]
        quesres = quesres.replace('<strong>', '')
        quesres = quesres.replace('</strong>', '')
        ques.append(quesres.replace('\n',''))

        ansres = test_str[ridx1 + len(ansub1): ridx2]
        ansres = ansres.replace('<strong>', '')
        ansres = ansres.replace('</strong>', '')
        ans.append(ansres)

        test_str=test_str.replace(quesub1,'',1)
        test_str=test_str.replace(quesub2,'',1)
        test_str=test_str.replace(ansub1,'',1)
        test_str=test_str.replace(ansub2,'',1)

output='''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": ['''

for i in range(len(ques)):
    if (i==len(ques)-1):
        output = output+'''{
            "@type": "Question",
            "name": "''' + ques[i] + '",'+ '''
            "acceptedAnswer": {
          "@type": "Answer",
          "text": "''' + ans[i] + '"\n}\n}]\n}\n</script>'
    else:
        output = output+'''{
            "@type": "Question",
            "name": "''' + ques[i] + '",'+ '''
            "acceptedAnswer": {
          "@type": "Answer",
          "text": "''' + ans[i] + '"\n}\n},'

print(output)
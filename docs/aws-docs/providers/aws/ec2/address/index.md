---
title: address
hide_title: false
hide_table_of_contents: false
keywords:
  - address
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>address</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.address</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `address_Allocate` | `EXEC` |  | &lt;p&gt;Allocates an Elastic IP address to your Amazon Web Services account. After you allocate the Elastic IP address you can associate it with an instance or network interface. After you release an Elastic IP address, it is released to the IP address pool and can be allocated to a different Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can allocate an Elastic IP address from an address pool owned by Amazon Web Services or from an address pool created from a public IPv4 address range that you have brought to Amazon Web Services for use with your Amazon Web Services resources using bring your own IP addresses (BYOIP). For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html"&gt;Bring Your Own IP Addresses (BYOIP)&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;[EC2-VPC] If you release an Elastic IP address, you might be able to recover it. You cannot recover an Elastic IP address that you released after it is allocated to another Amazon Web Services account. You cannot recover an Elastic IP address for EC2-Classic. To attempt to recover an Elastic IP address that you released, specify it in this operation.&lt;/p&gt; &lt;p&gt;An Elastic IP address is for use either in the EC2-Classic platform or in a VPC. By default, you can allocate 5 Elastic IP addresses for EC2-Classic per Region and 5 Elastic IP addresses for EC2-VPC per Region.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html"&gt;Elastic IP Addresses&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can allocate a carrier IP address which is a public IP address from a telecommunication carrier, to a network interface which resides in a subnet in a Wavelength Zone (for example an EC2 instance). &lt;/p&gt; |
| `address_Associate` | `EXEC` |  | &lt;p&gt;Associates an Elastic IP address, or carrier IP address (for instances that are in subnets in Wavelength Zones) with an instance or a network interface. Before you can use an Elastic IP address, you must allocate it to your account.&lt;/p&gt; &lt;p&gt;An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html"&gt;Elastic IP Addresses&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;[EC2-Classic, VPC in an EC2-VPC-only account] If the Elastic IP address is already associated with a different instance, it is disassociated from that instance and associated with the specified instance. If you associate an Elastic IP address with an instance that has an existing Elastic IP address, the existing address is disassociated from the instance, but remains allocated to your account.&lt;/p&gt; &lt;p&gt;[VPC in an EC2-Classic account] If you don't specify a private IP address, the Elastic IP address is associated with the primary IP address. If the Elastic IP address is already associated with a different instance or a network interface, you get an error unless you allow reassociation. You cannot associate an Elastic IP address with an instance or network interface that has an existing Elastic IP address.&lt;/p&gt; &lt;p&gt;[Subnets in Wavelength Zones] You can associate an IP address from the telecommunication carrier to the instance or network interface. &lt;/p&gt; &lt;p&gt;You cannot associate an Elastic IP address with an interface in a different network border group.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error, and you may be charged for each time the Elastic IP address is remapped to the same instance. For more information, see the &lt;i&gt;Elastic IP Addresses&lt;/i&gt; section of &lt;a href="http://aws.amazon.com/ec2/pricing/"&gt;Amazon EC2 Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; |
| `address_Disassociate` | `EXEC` |  | &lt;p&gt;Disassociates an Elastic IP address from the instance or network interface it's associated with.&lt;/p&gt; &lt;p&gt;An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html"&gt;Elastic IP Addresses&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error.&lt;/p&gt; |
| `address_Release` | `EXEC` |  | &lt;p&gt;Releases the specified Elastic IP address.&lt;/p&gt; &lt;p&gt;[EC2-Classic, default VPC] Releasing an Elastic IP address automatically disassociates it from any instance that it's associated with. To disassociate an Elastic IP address without releasing it, use &lt;a&gt;DisassociateAddress&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;[Nondefault VPC] You must use &lt;a&gt;DisassociateAddress&lt;/a&gt; to disassociate the Elastic IP address before you can release it. Otherwise, Amazon EC2 returns an error (&lt;code&gt;InvalidIPAddress.InUse&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;After releasing an Elastic IP address, it is released to the IP address pool. Be sure to update your DNS records and any servers or devices that communicate with the address. If you attempt to release an Elastic IP address that you already released, you'll get an &lt;code&gt;AuthFailure&lt;/code&gt; error if the address is already allocated to another Amazon Web Services account.&lt;/p&gt; &lt;p&gt;[EC2-VPC] After you release an Elastic IP address for use in a VPC, you might be able to recover it. For more information, see &lt;a&gt;AllocateAddress&lt;/a&gt;.&lt;/p&gt; |

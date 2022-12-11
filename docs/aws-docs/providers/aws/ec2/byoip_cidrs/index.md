---
title: byoip_cidrs
hide_title: false
hide_table_of_contents: false
keywords:
  - byoip_cidrs
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
<tr><td><b>Name</b></td><td><code>byoip_cidrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.byoip_cidrs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the address range. |
| `cidr` | `string` | The address range, in CIDR notation. |
| `state` | `string` | The state of the address pool. |
| `statusMessage` | `string` | Upon success, contains the ID of the address pool. Otherwise, contains an error message. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `byoip_cidrs_Describe` | `SELECT` | `MaxResults` | &lt;p&gt;Describes the IP address ranges that were specified in calls to &lt;a&gt;ProvisionByoipCidr&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To describe the address pools that were created when you provisioned the address ranges, use &lt;a&gt;DescribePublicIpv4Pools&lt;/a&gt; or &lt;a&gt;DescribeIpv6Pools&lt;/a&gt;.&lt;/p&gt; |
| `byoip_cidr_Advertise` | `EXEC` | `Cidr` | &lt;p&gt;Advertises an IPv4 or IPv6 address range that is provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP).&lt;/p&gt; &lt;p&gt;You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time.&lt;/p&gt; &lt;p&gt;We recommend that you stop advertising the BYOIP CIDR from other locations when you advertise it from Amazon Web Services. To minimize down time, you can configure your Amazon Web Services resources to use an address from a BYOIP CIDR before it is advertised, and then simultaneously stop advertising it from the current location and start advertising it through Amazon Web Services.&lt;/p&gt; &lt;p&gt;It can take a few minutes before traffic to the specified addresses starts routing to Amazon Web Services because of BGP propagation delays.&lt;/p&gt; &lt;p&gt;To stop advertising the BYOIP CIDR, use &lt;a&gt;WithdrawByoipCidr&lt;/a&gt;.&lt;/p&gt; |
| `byoip_cidr_Deprovision` | `EXEC` | `Cidr` | &lt;p&gt;Releases the specified address range that you provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool.&lt;/p&gt; &lt;p&gt;Before you can release an address range, you must stop advertising it using &lt;a&gt;WithdrawByoipCidr&lt;/a&gt; and you must not have any IP addresses allocated from its address range.&lt;/p&gt; |
| `byoip_cidr_Provision` | `EXEC` | `Cidr` | &lt;p&gt;Provisions an IPv4 or IPv6 address range for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range is provisioned, it is ready to be advertised using &lt;a&gt;AdvertiseByoipCidr&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Amazon Web Services verifies that you own the address range and are authorized to advertise it. You must ensure that the address range is registered to you and that you created an RPKI ROA to authorize Amazon ASNs 16509 and 14618 to advertise the address range. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html"&gt;Bring your own IP addresses (BYOIP)&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Provisioning an address range is an asynchronous operation, so the call returns immediately, but the address range is not ready to use until its status changes from &lt;code&gt;pending-provision&lt;/code&gt; to &lt;code&gt;provisioned&lt;/code&gt;. To monitor the status of an address range, use &lt;a&gt;DescribeByoipCidrs&lt;/a&gt;. To allocate an Elastic IP address from your IPv4 address pool, use &lt;a&gt;AllocateAddress&lt;/a&gt; with either the specific address from the address pool or the ID of the address pool.&lt;/p&gt; |
| `byoip_cidr_Withdraw` | `EXEC` | `Cidr` | &lt;p&gt;Stops advertising an address range that is provisioned as an address pool.&lt;/p&gt; &lt;p&gt;You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time.&lt;/p&gt; &lt;p&gt;It can take a few minutes before traffic to the specified addresses stops routing to Amazon Web Services because of BGP propagation delays.&lt;/p&gt; |

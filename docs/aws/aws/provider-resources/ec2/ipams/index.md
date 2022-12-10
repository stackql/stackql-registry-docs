---
title: ipams
hide_title: false
hide_table_of_contents: false
keywords:
  - ipams
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
<tr><td><b>Name</b></td><td><code>ipams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description for the IPAM. |
| `ipamArn` | `string` | The ARN of the IPAM. |
| `ipamRegion` | `string` | The Amazon Web Services Region of the IPAM. |
| `ownerId` | `string` | The Amazon Web Services account ID of the owner of the IPAM. |
| `publicDefaultScopeId` | `string` | The ID of the IPAM's default public scope. |
| `tagSet` | `array` | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key &lt;code&gt;Owner&lt;/code&gt; and the value &lt;code&gt;TeamA&lt;/code&gt;, specify &lt;code&gt;tag:Owner&lt;/code&gt; for the filter name and &lt;code&gt;TeamA&lt;/code&gt; for the filter value. |
| `operatingRegionSet` | `array` | &lt;p&gt;The operating Regions for an IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.&lt;/p&gt; &lt;p&gt;For more information about operating Regions, see &lt;a href="/vpc/latest/ipam/create-ipam.html"&gt;Create an IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `scopeCount` | `integer` | The number of scopes in the IPAM. The scope quota is 5. For more information on quotas, see &lt;a href="/vpc/latest/ipam/quotas-ipam.html"&gt;Quotas in IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.  |
| `ipamId` | `string` | The ID of the IPAM. |
| `state` | `string` | The state of the IPAM. |
| `privateDefaultScopeId` | `string` | The ID of the IPAM's default private scope. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ipams_Describe` | `SELECT` |  | &lt;p&gt;Get information about your IPAM pools.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/what-is-it-ipam.html"&gt;What is IPAM?&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| `ipam_Create` | `INSERT` |  | &lt;p&gt;Create an IPAM. Amazon VPC IP Address Manager (IPAM) is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across Amazon Web Services Regions and accounts throughout your Amazon Web Services Organization.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/create-ipam.html"&gt;Create an IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| `ipam_Delete` | `DELETE` | `IpamId` | &lt;p&gt;Delete an IPAM. Deleting an IPAM removes all monitored data associated with the IPAM including the historical data for CIDRs.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/delete-ipam.html"&gt;Delete an IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| `ipam_Modify` | `EXEC` | `IpamId` | Modify the configurations of an IPAM.  |

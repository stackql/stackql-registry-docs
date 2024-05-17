---
title: ipams
hide_title: false
hide_table_of_contents: false
keywords:
  - ipams
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.ipams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | The description for the IPAM. |
| <CopyableCode code="ipamArn" /> | `string` | The ARN of the IPAM. |
| <CopyableCode code="ipamId" /> | `string` | The ID of the IPAM. |
| <CopyableCode code="ipamRegion" /> | `string` | The Amazon Web Services Region of the IPAM. |
| <CopyableCode code="operatingRegionSet" /> | `array` | &lt;p&gt;The operating Regions for an IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.&lt;/p&gt; &lt;p&gt;For more information about operating Regions, see &lt;a href="/vpc/latest/ipam/create-ipam.html"&gt;Create an IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="ownerId" /> | `string` | The Amazon Web Services account ID of the owner of the IPAM. |
| <CopyableCode code="privateDefaultScopeId" /> | `string` | The ID of the IPAM's default private scope. |
| <CopyableCode code="publicDefaultScopeId" /> | `string` | The ID of the IPAM's default public scope. |
| <CopyableCode code="scopeCount" /> | `integer` | The number of scopes in the IPAM. The scope quota is 5. For more information on quotas, see &lt;a href="/vpc/latest/ipam/quotas-ipam.html"&gt;Quotas in IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.  |
| <CopyableCode code="state" /> | `string` | The state of the IPAM. |
| <CopyableCode code="tagSet" /> | `array` | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key &lt;code&gt;Owner&lt;/code&gt; and the value &lt;code&gt;TeamA&lt;/code&gt;, specify &lt;code&gt;tag:Owner&lt;/code&gt; for the filter name and &lt;code&gt;TeamA&lt;/code&gt; for the filter value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="ipams_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Get information about your IPAM pools.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/what-is-it-ipam.html"&gt;What is IPAM?&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| <CopyableCode code="ipam_Create" /> | `INSERT` | <CopyableCode code="region" /> | &lt;p&gt;Create an IPAM. Amazon VPC IP Address Manager (IPAM) is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across Amazon Web Services Regions and accounts throughout your Amazon Web Services Organization.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/create-ipam.html"&gt;Create an IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| <CopyableCode code="ipam_Delete" /> | `DELETE` | <CopyableCode code="IpamId, region" /> | &lt;p&gt;Delete an IPAM. Deleting an IPAM removes all monitored data associated with the IPAM including the historical data for CIDRs.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/delete-ipam.html"&gt;Delete an IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| <CopyableCode code="ipam_Modify" /> | `EXEC` | <CopyableCode code="IpamId, region" /> | Modify the configurations of an IPAM.  |

---
title: availability_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_zones
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
<tr><td><b>Name</b></td><td><code>availability_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.availability_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groupName" /> | `string` | &lt;p&gt; For Availability Zones, this parameter has the same value as the Region name.&lt;/p&gt; &lt;p&gt;For Local Zones, the name of the associated group, for example &lt;code&gt;us-west-2-lax-1&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For Wavelength Zones, the name of the associated group, for example &lt;code&gt;us-east-1-wl1-bos-wlz-1&lt;/code&gt;.&lt;/p&gt; |
| <CopyableCode code="messageSet" /> | `array` | Any messages about the Availability Zone, Local Zone, or Wavelength Zone. |
| <CopyableCode code="networkBorderGroup" /> | `string` | The name of the network border group. |
| <CopyableCode code="optInStatus" /> | `string` | &lt;p&gt;For Availability Zones, this parameter always has the value of &lt;code&gt;opt-in-not-required&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For Local Zones and Wavelength Zones, this parameter is the opt-in status. The possible values are &lt;code&gt;opted-in&lt;/code&gt;, and &lt;code&gt;not-opted-in&lt;/code&gt;.&lt;/p&gt; |
| <CopyableCode code="parentZoneId" /> | `string` | The ID of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls. |
| <CopyableCode code="parentZoneName" /> | `string` | The name of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls. |
| <CopyableCode code="regionName" /> | `string` | The name of the Region. |
| <CopyableCode code="zoneId" /> | `string` | The ID of the Availability Zone, Local Zone, or Wavelength Zone. |
| <CopyableCode code="zoneName" /> | `string` | The name of the Availability Zone, Local Zone, or Wavelength Zone. |
| <CopyableCode code="zoneState" /> | `string` | The state of the Availability Zone, Local Zone, or Wavelength Zone. This value is always &lt;code&gt;available&lt;/code&gt;. |
| <CopyableCode code="zoneType" /> | `string` | The type of zone. The valid values are &lt;code&gt;availability-zone&lt;/code&gt;, &lt;code&gt;local-zone&lt;/code&gt;, and &lt;code&gt;wavelength-zone&lt;/code&gt;. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="availability_zones_Describe" /> | `SELECT` | <CopyableCode code="region" /> |

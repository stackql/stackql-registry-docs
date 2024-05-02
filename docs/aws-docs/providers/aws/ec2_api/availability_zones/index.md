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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>availability_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.availability_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `groupName` | `string` | &lt;p&gt; For Availability Zones, this parameter has the same value as the Region name.&lt;/p&gt; &lt;p&gt;For Local Zones, the name of the associated group, for example &lt;code&gt;us-west-2-lax-1&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For Wavelength Zones, the name of the associated group, for example &lt;code&gt;us-east-1-wl1-bos-wlz-1&lt;/code&gt;.&lt;/p&gt; |
| `messageSet` | `array` | Any messages about the Availability Zone, Local Zone, or Wavelength Zone. |
| `networkBorderGroup` | `string` | The name of the network border group. |
| `optInStatus` | `string` | &lt;p&gt;For Availability Zones, this parameter always has the value of &lt;code&gt;opt-in-not-required&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For Local Zones and Wavelength Zones, this parameter is the opt-in status. The possible values are &lt;code&gt;opted-in&lt;/code&gt;, and &lt;code&gt;not-opted-in&lt;/code&gt;.&lt;/p&gt; |
| `parentZoneId` | `string` | The ID of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls. |
| `parentZoneName` | `string` | The name of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls. |
| `regionName` | `string` | The name of the Region. |
| `zoneId` | `string` | The ID of the Availability Zone, Local Zone, or Wavelength Zone. |
| `zoneName` | `string` | The name of the Availability Zone, Local Zone, or Wavelength Zone. |
| `zoneState` | `string` | The state of the Availability Zone, Local Zone, or Wavelength Zone. This value is always &lt;code&gt;available&lt;/code&gt;. |
| `zoneType` | `string` | The type of zone. The valid values are &lt;code&gt;availability-zone&lt;/code&gt;, &lt;code&gt;local-zone&lt;/code&gt;, and &lt;code&gt;wavelength-zone&lt;/code&gt;. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `availability_zones_Describe` | `SELECT` | `region` |

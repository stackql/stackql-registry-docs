---
title: ip_geodata
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_geodata
  - security_insights
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_geodata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.ip_geodata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `organization` | `string` | The name of the organization for this IP address |
| `latitude` | `string` | The latitude of this IP address |
| `region` | `string` | The geographic region this IP address is located in |
| `asn` | `string` | The autonomous system number associated with this IP address |
| `stateCode` | `string` | The abbreviated name for the state this IP address is located in |
| `state` | `string` | The state this IP address is located in |
| `ipAddr` | `string` | The dotted-decimal or colon-separated string representation of the IP address |
| `continent` | `string` | The continent this IP address is located on |
| `city` | `string` | The city this IP address is located in |
| `stateCf` | `integer` | A numeric rating of confidence that the value in the 'state' field is correct on a scale of 0-100 |
| `ipRoutingType` | `string` | A description of the connection type of this IP address |
| `longitude` | `string` | The longitude of this IP address |
| `organizationType` | `string` | The type of the organization for this IP address |
| `cityCf` | `integer` | A numeric rating of confidence that the value in the 'city' field is correct, on a scale of 0-100 |
| `countryCf` | `integer` | A numeric rating of confidence that the value in the 'country' field is correct on a scale of 0-100 |
| `country` | `string` | The county this IP address is located in |
| `carrier` | `string` | The name of the carrier for this IP address |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `IPGeodata_Get` | `SELECT` | `ipAddress, resourceGroupName, subscriptionId` |

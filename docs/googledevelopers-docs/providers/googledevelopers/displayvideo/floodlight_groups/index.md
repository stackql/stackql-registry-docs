---
title: floodlight_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - floodlight_groups
  - displayvideo
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>floodlight_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.floodlight_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the Floodlight group. |
| `webTagType` | `string` | Required. The web tag type enabled for the Floodlight group. |
| `activeViewConfig` | `object` | Configuration for custom Active View video viewability metrics. |
| `customVariables` | `object` | User-defined custom variables owned by the Floodlight group. Use custom Floodlight variables to create reporting data that is tailored to your unique business needs. Custom Floodlight variables use the keys `U1=`, `U2=`, and so on, and can take any values that you choose to pass to them. You can use them to track virtually any type of data that you collect about your customers, such as the genre of movie that a customer purchases, the country to which the item is shipped, and so on. Custom Floodlight variables may not be used to pass any data that could be used or recognized as personally identifiable information (PII). Example: `custom_variables &#123; fields &#123; "U1": value &#123; number_value: 123.4 &#125;, "U2": value &#123; string_value: "MyVariable2" &#125;, "U3": value &#123; string_value: "MyVariable3" &#125; &#125; &#125;` Acceptable values for keys are "U1" through "U100", inclusive. String values must be less than 64 characters long, and cannot contain the following characters: `"&lt;&gt;`. |
| `displayName` | `string` | Required. The display name of the Floodlight group. |
| `floodlightGroupId` | `string` | Output only. The unique ID of the Floodlight group. Assigned by the system. |
| `lookbackWindow` | `object` | Specifies how many days into the past to look when determining whether to record a conversion. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `floodlightGroups_get` | `SELECT` | `floodlightGroupsId` | Gets a Floodlight group. |
| `floodlightGroups_patch` | `EXEC` | `floodlightGroupId` | Updates an existing Floodlight group. Returns the updated Floodlight group if successful. |

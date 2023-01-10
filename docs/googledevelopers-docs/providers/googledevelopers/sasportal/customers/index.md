---
title: customers
hide_title: false
hide_table_of_contents: false
keywords:
  - customers
  - sasportal
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
<tr><td><b>Name</b></td><td><code>customers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.sasportal.customers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the customer. |
| `displayName` | `string` | Required. Name of the organization that the customer entity represents. |
| `sasUserIds` | `array` | User IDs used by the devices belonging to this customer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customersId` | Returns a requested customer. |
| `list` | `SELECT` |  | Returns a list of requested customers. |
| `patch` | `EXEC` | `customersId` | Updates an existing customer. |

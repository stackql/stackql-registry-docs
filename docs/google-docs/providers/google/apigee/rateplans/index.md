---
title: rateplans
hide_title: false
hide_table_of_contents: false
keywords:
  - rateplans
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rateplans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.rateplans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextStartKey` | `string` | Value that can be sent as `startKey` to retrieve the next page of content. If this field is omitted, there are no subsequent pages. |
| `ratePlans` | `array` | List of rate plans in an organization. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_apiproducts_rateplans_get` | `SELECT` | `apiproductsId, organizationsId, rateplansId` | Gets the details of a rate plan. |
| `organizations_apiproducts_rateplans_list` | `SELECT` | `apiproductsId, organizationsId` | Lists all the rate plans for an API product. |
| `organizations_apiproducts_rateplans_create` | `INSERT` | `apiproductsId, organizationsId` | Create a rate plan that is associated with an API product in an organization. Using rate plans, API product owners can monetize their API products by configuring one or more of the following: - Billing frequency - Initial setup fees for using an API product - Payment funding model (postpaid only) - Fixed recurring or consumption-based charges for using an API product - Revenue sharing with developer partners An API product can have multiple rate plans associated with it but *only one* rate plan can be active at any point of time. **Note: From the developer's perspective, they purchase API products not rate plans. |
| `organizations_apiproducts_rateplans_delete` | `DELETE` | `apiproductsId, organizationsId, rateplansId` | Deletes a rate plan. |
| `organizations_apiproducts_rateplans_update` | `EXEC` | `apiproductsId, organizationsId, rateplansId` | Updates an existing rate plan. |

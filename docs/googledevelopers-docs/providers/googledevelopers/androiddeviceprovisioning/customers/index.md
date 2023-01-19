---
title: customers
hide_title: false
hide_table_of_contents: false
keywords:
  - customers
  - androiddeviceprovisioning
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
<tr><td><b>Id</b></td><td><code>googledevelopers.androiddeviceprovisioning.customers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalSize` | `integer` | The total count of items in the list irrespective of pagination. |
| `customers` | `array` | List of customers of the vendor. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Omitted if no further results are available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` |  | Lists the user's customer accounts. |
| `partners_customers_list` | `SELECT` | `partnersId` | Lists the customers that are enrolled to the reseller identified by the `partnerId` argument. This list includes customers that the reseller created and customers that enrolled themselves using the portal. |
| `partners_vendors_customers_list` | `SELECT` | `partnersId, vendorsId` | Lists the customers of the vendor. |
| `partners_customers_create` | `INSERT` | `partnersId` | Creates a customer for zero-touch enrollment. After the method returns successfully, admin and owner roles can manage devices and EMM configs by calling API methods or using their zero-touch enrollment portal. The customer receives an email that welcomes them to zero-touch enrollment and explains how to sign into the portal. |

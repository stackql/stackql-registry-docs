---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androiddeviceprovisioning.configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The API resource name in the format `customers/[CUSTOMER_ID]/configurations/[CONFIGURATION_ID]`. Assigned by the server. |
| `contactEmail` | `string` | Required. The email address that device users can contact to get help. Zero-touch enrollment shows this email address to device users before device provisioning. The value is validated on input. |
| `contactPhone` | `string` | Required. The telephone number that device users can call, using another device, to get help. Zero-touch enrollment shows this number to device users before device provisioning. Accepts numerals, spaces, the plus sign, hyphens, and parentheses. |
| `companyName` | `string` | Required. The name of the organization. Zero-touch enrollment shows this organization name to device users during device provisioning. |
| `dpcExtras` | `string` | The JSON-formatted EMM provisioning extras that are passed to the DPC. |
| `dpcResourcePath` | `string` | Required. The resource name of the selected DPC (device policy controller) in the format `customers/[CUSTOMER_ID]/dpcs/*`. To list the supported DPCs, call `customers.dpcs.list`. |
| `configurationId` | `string` | Output only. The ID of the configuration. Assigned by the server. |
| `isDefault` | `boolean` | Required. Whether this is the default configuration that zero-touch enrollment applies to any new devices the organization purchases in the future. Only one customer configuration can be the default. Setting this value to `true`, changes the previous default configuration's `isDefault` value to `false`. |
| `customMessage` | `string` | A message, containing one or two sentences, to help device users get help or give them more details about what’s happening to their device. Zero-touch enrollment shows this message before the device is provisioned. |
| `configurationName` | `string` | Required. A short name that describes the configuration's purpose. For example, _Sales team_ or _Temporary employees_. The zero-touch enrollment portal displays this name to IT admins. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_configurations_get` | `SELECT` | `configurationsId, customersId` | Gets the details of a configuration. |
| `customers_configurations_list` | `SELECT` | `customersId` | Lists a customer's configurations. |
| `customers_configurations_create` | `INSERT` | `customersId` | Creates a new configuration. Once created, a customer can apply the configuration to devices. |
| `customers_configurations_delete` | `DELETE` | `configurationsId, customersId` | Deletes an unused configuration. The API call fails if the customer has devices with the configuration applied. |
| `customers_configurations_patch` | `EXEC` | `configurationsId, customersId` | Updates a configuration's field values. |

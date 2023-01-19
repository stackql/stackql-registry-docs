---
title: advertisers
hide_title: false
hide_table_of_contents: false
keywords:
  - advertisers
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
<tr><td><b>Name</b></td><td><code>advertisers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.advertisers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the advertiser. |
| `prismaEnabled` | `boolean` | Whether integration with Mediaocean (Prisma) is enabled. By enabling this, you agree to the following: On behalf of my company, I authorize Mediaocean (Prisma) to send budget segment plans to Google, and I authorize Google to send corresponding reporting and invoices from DV360 to Mediaocean for the purposes of budget planning, billing, and reconciliation for this advertiser. |
| `updateTime` | `string` | Output only. The timestamp when the advertiser was last updated. Assigned by the system. |
| `partnerId` | `string` | Required. Immutable. The unique ID of the partner that the advertiser belongs to. |
| `servingConfig` | `object` | Targeting settings related to ad serving of an advertiser. |
| `billingConfig` | `object` | Billing related settings of an advertiser. |
| `entityStatus` | `string` | Required. Controls whether or not insertion orders and line items of the advertiser can spend their budgets and bid on inventory. * Accepted values are `ENTITY_STATUS_ACTIVE`, `ENTITY_STATUS_PAUSED` and `ENTITY_STATUS_SCHEDULED_FOR_DELETION`. * If set to `ENTITY_STATUS_SCHEDULED_FOR_DELETION`, the advertiser will be deleted 30 days from when it was first scheduled for deletion. |
| `generalConfig` | `object` | General settings of an advertiser. |
| `dataAccessConfig` | `object` | Settings that control how advertiser related data may be accessed. |
| `creativeConfig` | `object` | Creatives related settings of an advertiser. |
| `displayName` | `string` | Required. The display name of the advertiser. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `adServerConfig` | `object` | Ad server related settings of an advertiser. |
| `advertiserId` | `string` | Output only. The unique ID of the advertiser. Assigned by the system. |
| `integrationDetails` | `object` | Integration details of an entry. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `advertisersId` | Gets an advertiser. |
| `list` | `SELECT` |  | Lists advertisers that are accessible to the current user. The order is defined by the order_by parameter. A single partner_id is required. Cross-partner listing is not supported. |
| `create` | `INSERT` |  | Creates a new advertiser. Returns the newly created advertiser if successful. This method can take up to 180 seconds to complete. |
| `delete` | `DELETE` | `advertisersId` | Deletes an advertiser. Deleting an advertiser will delete all of its child resources, for example, campaigns, insertion orders and line items. A deleted advertiser cannot be recovered. |
| `audit` | `EXEC` | `advertisersId` | Audits an advertiser. Returns the counts of used entities per resource type under the advertiser provided. Used entities count towards their respective resource limit. See https://support.google.com/displayvideo/answer/6071450. |
| `editAssignedTargetingOptions` | `EXEC` | `advertisersId` | Edits targeting options under a single advertiser. The operation will delete the assigned targeting options provided in BulkEditAdvertiserAssignedTargetingOptionsRequest.delete_requests and then create the assigned targeting options provided in BulkEditAdvertiserAssignedTargetingOptionsRequest.create_requests . |
| `patch` | `EXEC` | `advertisersId` | Updates an existing advertiser. Returns the updated advertiser if successful. |

---
title: sfdc_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - sfdc_channels
  - integrations
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
<tr><td><b>Name</b></td><td><code>sfdc_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.sfdc_channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the SFDC channel projects/&#123;project&#125;/locations/&#123;location&#125;/sfdcInstances/&#123;sfdc_instance&#125;/sfdcChannels/&#123;sfdc_channel&#125;. |
| `description` | `string` | The description for this channel |
| `isActive` | `boolean` | Indicated if a channel has any active integrations referencing it. Set to false when the channel is created, and set to true if there is any integration published with the channel configured in it. |
| `displayName` | `string` | Client level unique name/alias to easily reference a channel. |
| `updateTime` | `string` | Output only. Time when the channel was last updated |
| `channelTopic` | `string` | The Channel topic defined by salesforce once an channel is opened |
| `deleteTime` | `string` | Output only. Time when the channel was deleted. Empty if not deleted. |
| `lastReplayId` | `string` | Last sfdc messsage replay id for channel |
| `createTime` | `string` | Output only. Time when the channel is created |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_products_sfdc_instances_sfdc_channels_get` | `SELECT` | `locationsId, productsId, projectsId, sfdcChannelsId, sfdcInstancesId` | Gets an sfdc channel. If the channel doesn't exist, Code.NOT_FOUND exception will be thrown. |
| `projects_locations_products_sfdc_instances_sfdc_channels_list` | `SELECT` | `locationsId, productsId, projectsId, sfdcInstancesId` | Lists all sfdc channels that match the filter. Restrict to sfdc channels belonging to the current client only. |
| `projects_locations_sfdc_instances_sfdc_channels_get` | `SELECT` | `locationsId, projectsId, sfdcChannelsId, sfdcInstancesId` | Gets an sfdc channel. If the channel doesn't exist, Code.NOT_FOUND exception will be thrown. |
| `projects_locations_sfdc_instances_sfdc_channels_list` | `SELECT` | `locationsId, projectsId, sfdcInstancesId` | Lists all sfdc channels that match the filter. Restrict to sfdc channels belonging to the current client only. |
| `projects_locations_products_sfdc_instances_sfdc_channels_create` | `INSERT` | `locationsId, productsId, projectsId, sfdcInstancesId` | Creates an sfdc channel record. Store the sfdc channel in Spanner. Returns the sfdc channel. |
| `projects_locations_sfdc_instances_sfdc_channels_create` | `INSERT` | `locationsId, projectsId, sfdcInstancesId` | Creates an sfdc channel record. Store the sfdc channel in Spanner. Returns the sfdc channel. |
| `projects_locations_products_sfdc_instances_sfdc_channels_delete` | `DELETE` | `locationsId, productsId, projectsId, sfdcChannelsId, sfdcInstancesId` | Deletes an sfdc channel. |
| `projects_locations_sfdc_instances_sfdc_channels_delete` | `DELETE` | `locationsId, projectsId, sfdcChannelsId, sfdcInstancesId` | Deletes an sfdc channel. |
| `_projects_locations_products_sfdc_instances_sfdc_channels_list` | `EXEC` | `locationsId, productsId, projectsId, sfdcInstancesId` | Lists all sfdc channels that match the filter. Restrict to sfdc channels belonging to the current client only. |
| `_projects_locations_sfdc_instances_sfdc_channels_list` | `EXEC` | `locationsId, projectsId, sfdcInstancesId` | Lists all sfdc channels that match the filter. Restrict to sfdc channels belonging to the current client only. |
| `projects_locations_products_sfdc_instances_sfdc_channels_patch` | `EXEC` | `locationsId, productsId, projectsId, sfdcChannelsId, sfdcInstancesId` | Updates an sfdc channel. Updates the sfdc channel in spanner. Returns the sfdc channel. |
| `projects_locations_sfdc_instances_sfdc_channels_patch` | `EXEC` | `locationsId, projectsId, sfdcChannelsId, sfdcInstancesId` | Updates an sfdc channel. Updates the sfdc channel in spanner. Returns the sfdc channel. |

---
title: ingestion_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - ingestion_settings
  - security
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
<tr><td><b>Name</b></td><td><code>ingestion_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.ingestion_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Ingestion setting data |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IngestionSettings_Get` | `SELECT` | `api-version, ingestionSettingName, subscriptionId` | Settings for ingesting security data and logs to correlate with resources associated with the subscription. |
| `IngestionSettings_List` | `SELECT` | `api-version, subscriptionId` | Settings for ingesting security data and logs to correlate with resources associated with the subscription. |
| `IngestionSettings_Create` | `INSERT` | `api-version, ingestionSettingName, subscriptionId` | Create setting for ingesting security data and logs to correlate with resources associated with the subscription. |
| `IngestionSettings_Delete` | `DELETE` | `api-version, ingestionSettingName, subscriptionId` | Deletes the ingestion settings for this subscription. |
| `IngestionSettings_ListConnectionStrings` | `EXEC` | `api-version, ingestionSettingName, subscriptionId` | Connection strings for ingesting security scan logs and data. |
| `IngestionSettings_ListTokens` | `EXEC` | `api-version, ingestionSettingName, subscriptionId` | Returns the token that is used for correlating ingested telemetry with the resources in the subscription. |

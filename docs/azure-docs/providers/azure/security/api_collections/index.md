---
title: api_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - api_collections
  - security
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>api_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.api_collections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_collections', value: 'view', },
        { label: 'api_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="base_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovered_via" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_api_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_api_endpoints_with_sensitive_data_exposed" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_external_api_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_inactive_api_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_unauthenticated_api_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sensitivity_label" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an API collection. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_azure_api_management_service" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Gets an Azure API Management API if it has been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected. |
| <CopyableCode code="list_by_azure_api_management_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets a list of Azure API Management APIs that have been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of API collections within a resource group that have been onboarded to Microsoft Defender for APIs. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of API collections within a subscription that have been onboarded to Microsoft Defender for APIs. |
| <CopyableCode code="offboard_azure_api_management_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Offboard an Azure API Management API from Microsoft Defender for APIs. The system will stop monitoring the operations within the Azure API Management API for intrusive behaviors. |
| <CopyableCode code="onboard_azure_api_management_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Onboard an Azure API Management API to Microsoft Defender for APIs. The system will start monitoring the operations within the Azure Management API for intrusive behaviors and provide alerts for attacks that have been detected. |

## `SELECT` examples

Gets a list of API collections within a subscription that have been onboarded to Microsoft Defender for APIs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_collections', value: 'view', },
        { label: 'api_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
apiId,
base_url,
discovered_via,
display_name,
number_of_api_endpoints,
number_of_api_endpoints_with_sensitive_data_exposed,
number_of_external_api_endpoints,
number_of_inactive_api_endpoints,
number_of_unauthenticated_api_endpoints,
provisioning_state,
resourceGroupName,
sensitivity_label,
serviceName,
subscriptionId,
type
FROM azure.security.vw_api_collections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.api_collections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


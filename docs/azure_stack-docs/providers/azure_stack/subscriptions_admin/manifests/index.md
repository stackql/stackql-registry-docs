---
title: manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - manifests
  - subscriptions_admin
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

Creates, updates, deletes, gets or lists a <code>manifests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.manifests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the registration. |
| <CopyableCode code="alwaysRoutable" /> | `boolean` | A value indicating whether the manifest is always routable by all subscriptions. |
| <CopyableCode code="displayName" /> | `string` | The display name. |
| <CopyableCode code="enabled" /> | `boolean` | A value indicating whether this resource provider is enabled. |
| <CopyableCode code="extensionCollection" /> | `object` | The manifest extension collection definition. |
| <CopyableCode code="linkedNotificationRules" /> | `object` | List of the linked notification rules. |
| <CopyableCode code="metadata" /> | `object` | The metadata. |
| <CopyableCode code="namespace" /> | `string` | The namespace. |
| <CopyableCode code="providerAuthorization" /> | `object` | The resource provider authorization information. |
| <CopyableCode code="providerLocation" /> | `string` | The location of the provider. |
| <CopyableCode code="providerType" /> | `string` | The resource provider type. |
| <CopyableCode code="provisioningState" /> | `string` | The provisioning state. |
| <CopyableCode code="resourceGroupName" /> | `string` | The name of the resource group. |
| <CopyableCode code="resourceHydrationAccounts" /> | `object` | List of the resource hydration accounts. |
| <CopyableCode code="resourceLocation" /> | `string` | The location of the resource. |
| <CopyableCode code="resourceTags" /> | `object` | The resource tags. |
| <CopyableCode code="resourceTypes" /> | `object` | List of the resource types. |
| <CopyableCode code="routingResourceManagerType" /> | `string` | Resource manager type. |
| <CopyableCode code="subscriptionId" /> | `string` | The subscription ID under which RP is registered. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="manifestName, subscriptionId" /> | Get the specified manifest. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of all manifests. |

## `SELECT` examples

Get a list of all manifests.


```sql
SELECT
name,
alwaysRoutable,
displayName,
enabled,
extensionCollection,
linkedNotificationRules,
metadata,
namespace,
providerAuthorization,
providerLocation,
providerType,
provisioningState,
resourceGroupName,
resourceHydrationAccounts,
resourceLocation,
resourceTags,
resourceTypes,
routingResourceManagerType,
subscriptionId
FROM azure_stack.subscriptions_admin.manifests
WHERE subscriptionId = '{{ subscriptionId }}';
```
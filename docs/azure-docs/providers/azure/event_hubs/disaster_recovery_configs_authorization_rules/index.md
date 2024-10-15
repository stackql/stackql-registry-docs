---
title: disaster_recovery_configs_authorization_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - disaster_recovery_configs_authorization_rules
  - event_hubs
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

Creates, updates, deletes, gets or lists a <code>disaster_recovery_configs_authorization_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disaster_recovery_configs_authorization_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.disaster_recovery_configs_authorization_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Properties supplied to create or update AuthorizationRule |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alias, authorizationRuleName, namespaceName, resourceGroupName, subscriptionId" /> | Gets an AuthorizationRule for a Namespace by rule name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="alias, namespaceName, resourceGroupName, subscriptionId" /> | Gets a list of authorization rules for a Namespace. |

## `SELECT` examples

Gets a list of authorization rules for a Namespace.


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.event_hubs.disaster_recovery_configs_authorization_rules
WHERE alias = '{{ alias }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
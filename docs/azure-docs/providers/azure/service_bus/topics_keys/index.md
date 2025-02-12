---
title: topics_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - topics_keys
  - service_bus
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

Creates, updates, deletes, gets or lists a <code>topics_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_bus.topics_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aliasPrimaryConnectionString" /> | `string` | Primary connection string of the alias if GEO DR is enabled |
| <CopyableCode code="aliasSecondaryConnectionString" /> | `string` | Secondary  connection string of the alias if GEO DR is enabled |
| <CopyableCode code="keyName" /> | `string` | A string that describes the authorization rule. |
| <CopyableCode code="primaryConnectionString" /> | `string` | Primary connection string of the created namespace authorization rule. |
| <CopyableCode code="primaryKey" /> | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | Secondary connection string of the created namespace authorization rule. |
| <CopyableCode code="secondaryKey" /> | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, topicName" /> | Gets the primary and secondary connection strings for the topic. |

## `SELECT` examples

Gets the primary and secondary connection strings for the topic.


```sql
SELECT
aliasPrimaryConnectionString,
aliasSecondaryConnectionString,
keyName,
primaryConnectionString,
primaryKey,
secondaryConnectionString,
secondaryKey
FROM azure.service_bus.topics_keys
WHERE authorizationRuleName = '{{ authorizationRuleName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicName = '{{ topicName }}';
```
---
title: services_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - services_keys
  - communication
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

Creates, updates, deletes, gets or lists a <code>services_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.services_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primaryConnectionString" /> | `string` | CommunicationService connection string constructed via the primaryKey |
| <CopyableCode code="primaryKey" /> | `string` | The primary access key. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | CommunicationService connection string constructed via the secondaryKey |
| <CopyableCode code="secondaryKey" /> | `string` | The secondary access key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="communicationServiceName, resourceGroupName, subscriptionId" /> | Get the access keys of the CommunicationService resource. |

## `SELECT` examples

Get the access keys of the CommunicationService resource.


```sql
SELECT
primaryConnectionString,
primaryKey,
secondaryConnectionString,
secondaryKey
FROM azure.communication.services_keys
WHERE communicationServiceName = '{{ communicationServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
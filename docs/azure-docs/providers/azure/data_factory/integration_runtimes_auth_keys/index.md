---
title: integration_runtimes_auth_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes_auth_keys
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>integration_runtimes_auth_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtimes_auth_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.integration_runtimes_auth_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authKey1" /> | `string` | The primary integration runtime authentication key. |
| <CopyableCode code="authKey2" /> | `string` | The secondary integration runtime authentication key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Retrieves the authentication keys for an integration runtime. |

## `SELECT` examples

Retrieves the authentication keys for an integration runtime.


```sql
SELECT
authKey1,
authKey2
FROM azure.data_factory.integration_runtimes_auth_keys
WHERE factoryName = '{{ factoryName }}'
AND integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
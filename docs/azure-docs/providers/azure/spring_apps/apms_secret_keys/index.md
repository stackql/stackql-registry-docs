---
title: apms_secret_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - apms_secret_keys
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>apms_secret_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apms_secret_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.apms_secret_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apmName, resourceGroupName, serviceName, subscriptionId" /> | List keys of APM sensitive properties. |

## `SELECT` examples

List keys of APM sensitive properties.


```sql
SELECT
column_anon
FROM azure.spring_apps.apms_secret_keys
WHERE apmName = '{{ apmName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
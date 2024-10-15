---
title: web_services_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - web_services_keys
  - machine_learning
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

Creates, updates, deletes, gets or lists a <code>web_services_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_services_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.machine_learning.web_services_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primary" /> | `string` | The primary access key. |
| <CopyableCode code="secondary" /> | `string` | The secondary access key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, webServiceName" /> | Gets the access keys for the specified web service. |

## `SELECT` examples

Gets the access keys for the specified web service.


```sql
SELECT
primary,
secondary
FROM azure.machine_learning.web_services_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webServiceName = '{{ webServiceName }}';
```
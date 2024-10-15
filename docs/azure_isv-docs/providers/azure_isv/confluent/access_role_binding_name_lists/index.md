---
title: access_role_binding_name_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - access_role_binding_name_lists
  - confluent
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

Creates, updates, deletes, gets or lists a <code>access_role_binding_name_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_role_binding_name_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.access_role_binding_name_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `array` | List of role binding names |
| <CopyableCode code="kind" /> | `string` | Type of response |
| <CopyableCode code="metadata" /> | `object` | Metadata of the list |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
data,
kind,
metadata
FROM azure_isv.confluent.access_role_binding_name_lists
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
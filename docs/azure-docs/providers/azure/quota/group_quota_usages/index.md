---
title: group_quota_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_usages
  - quota
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

Creates, updates, deletes, gets or lists a <code>group_quota_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quota_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Resource details with usages and GroupQuota. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupQuotaName, location, managementGroupId, resourceProviderName" /> | Gets the GroupQuotas usages and limits(quota). Location is required paramter. |

## `SELECT` examples

Gets the GroupQuotas usages and limits(quota). Location is required paramter.


```sql
SELECT
properties
FROM azure.quota.group_quota_usages
WHERE groupQuotaName = '{{ groupQuotaName }}'
AND location = '{{ location }}'
AND managementGroupId = '{{ managementGroupId }}'
AND resourceProviderName = '{{ resourceProviderName }}';
```
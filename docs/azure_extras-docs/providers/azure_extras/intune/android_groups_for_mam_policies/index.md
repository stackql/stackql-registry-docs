---
title: android_groups_for_mam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - android_groups_for_mam_policies
  - intune
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

Creates, updates, deletes, gets or lists a <code>android_groups_for_mam_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>android_groups_for_mam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intune.android_groups_for_mam_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName, policyName" /> | Returns groups for a given AndroidMAMPolicy. |

## `SELECT` examples

Returns groups for a given AndroidMAMPolicy.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_extras.intune.android_groups_for_mam_policies
WHERE hostName = '{{ hostName }}'
AND policyName = '{{ policyName }}';
```
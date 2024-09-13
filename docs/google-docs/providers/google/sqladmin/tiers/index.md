
---
title: tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - tiers
  - sqladmin
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

Creates, updates, deletes or gets an <code>tier</code> resource or lists <code>tiers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.tiers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="DiskQuota" /> | `string` | The maximum disk size of this tier in bytes. |
| <CopyableCode code="RAM" /> | `string` | The maximum RAM usage of this tier in bytes. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#tier`. |
| <CopyableCode code="region" /> | `array` | The applicable regions for this tier. |
| <CopyableCode code="tier" /> | `string` | An identifier for the machine type, for example, `db-custom-1-3840`. For related information, see [Pricing](/sql/pricing). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Lists all available machine types (tiers) for Cloud SQL, for example, `db-custom-1-3840`. For more information, see https://cloud.google.com/sql/pricing. |

## `SELECT` examples

Lists all available machine types (tiers) for Cloud SQL, for example, `db-custom-1-3840`. For more information, see https://cloud.google.com/sql/pricing.

```sql
SELECT
DiskQuota,
RAM,
kind,
region,
tier
FROM google.sqladmin.tiers
WHERE project = '{{ project }}'; 
```

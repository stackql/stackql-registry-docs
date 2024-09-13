
---
title: admin_schemav2
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_schemav2
  - apigee
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

Creates, updates, deletes or gets an <code>admin_schemav2</code> resource or lists <code>admin_schemav2</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>admin_schemav2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.admin_schemav2" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dimensions" /> | `array` | List of schema fields grouped as dimensions. |
| <CopyableCode code="meta" /> | `array` | Additional metadata associated with schema. This is a legacy field and usually consists of an empty array of strings. |
| <CopyableCode code="metrics" /> | `array` | List of schema fields grouped as dimensions that can be used with an aggregate function such as `sum`, `avg`, `min`, and `max`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_analytics_admin_get_schemav2" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Gets a list of metrics and dimensions that can be used to create analytics queries and reports. Each schema element contains the name of the field, its associated type, and a flag indicating whether it is a standard or custom field. |

## `SELECT` examples

Gets a list of metrics and dimensions that can be used to create analytics queries and reports. Each schema element contains the name of the field, its associated type, and a flag indicating whether it is a standard or custom field.

```sql
SELECT
dimensions,
meta,
metrics
FROM google.apigee.admin_schemav2
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

---
title: alerts_externals
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_externals
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>alerts_externals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_externals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.alerts_externals" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="properties" /> | `object` | Alert properties. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="externalCloudProviderId, externalCloudProviderType" /> | Lists the Alerts for external cloud provider type defined. |

## `SELECT` examples

Lists the Alerts for external cloud provider type defined.


```sql
SELECT
id,
name,
eTag,
properties,
type
FROM azure.cost_management.alerts_externals
WHERE externalCloudProviderId = '{{ externalCloudProviderId }}'
AND externalCloudProviderType = '{{ externalCloudProviderType }}';
```
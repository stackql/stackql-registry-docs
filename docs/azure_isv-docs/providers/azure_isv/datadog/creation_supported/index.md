---
title: creation_supported
hide_title: false
hide_table_of_contents: false
keywords:
  - creation_supported
  - datadog
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

Creates, updates, deletes, gets or lists a <code>creation_supported</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>creation_supported</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.creation_supported" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Datadog resource can be created or not properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datadogOrganizationId, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datadogOrganizationId, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
properties
FROM azure_isv.datadog.creation_supported
WHERE datadogOrganizationId = '{{ datadogOrganizationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
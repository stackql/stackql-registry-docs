---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
  - eventarc
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

Creates, updates, deletes, gets or lists a <code>providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.eventarc.providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. In `projects/{project}/locations/{location}/providers/{provider_id}` format. |
| <CopyableCode code="displayName" /> | `string` | Output only. Human friendly name for the Provider. For example "Cloud Storage". |
| <CopyableCode code="eventTypes" /> | `array` | Output only. Event types for this provider. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, providersId" /> | Get a single Provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List providers. |

## `SELECT` examples

List providers.

```sql
SELECT
name,
displayName,
eventTypes
FROM google.eventarc.providers
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

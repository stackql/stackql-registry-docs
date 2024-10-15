---
title: rai_content_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_content_filters
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>rai_content_filters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rai_content_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.rai_content_filters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Azure OpenAI Content Filter Properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="filterName, location, subscriptionId" /> | Get Content Filters by Name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List Content Filters types. |

## `SELECT` examples

List Content Filters types.


```sql
SELECT
properties
FROM azure.cognitive_services.rai_content_filters
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
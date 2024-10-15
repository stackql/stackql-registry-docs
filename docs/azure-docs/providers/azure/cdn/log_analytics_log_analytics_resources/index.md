---
title: log_analytics_log_analytics_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics_log_analytics_resources
  - cdn
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

Creates, updates, deletes, gets or lists a <code>log_analytics_log_analytics_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_analytics_log_analytics_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.log_analytics_log_analytics_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="customDomains" /> | `array` |  |
| <CopyableCode code="endpoints" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Get all endpoints and custom domains available for AFD log report |

## `SELECT` examples

Get all endpoints and custom domains available for AFD log report


```sql
SELECT
customDomains,
endpoints
FROM azure.cdn.log_analytics_log_analytics_resources
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
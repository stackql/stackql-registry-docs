---
title: activities
hide_title: false
hide_table_of_contents: false
keywords:
  - activities
  - policyanalyzer
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

Creates, updates, deletes, gets or lists a <code>activities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.policyanalyzer.activities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activities" /> | `array` | The set of activities that match the filter included in the request. |
| <CopyableCode code="nextPageToken" /> | `string` | If there might be more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="query" /> | `SELECT` | <CopyableCode code="activityTypesId, locationsId, organizationsId" /> | Queries policy activities on Google Cloud resources. |

## `SELECT` examples

Queries policy activities on Google Cloud resources.

```sql
SELECT
activities,
nextPageToken
FROM google.policyanalyzer.activities
WHERE activityTypesId = '{{ activityTypesId }}'
AND locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}';
```

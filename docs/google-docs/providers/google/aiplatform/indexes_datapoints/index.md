
---
title: indexes_datapoints
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes_datapoints
  - aiplatform
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

Creates, updates, deletes or gets an <code>indexes_datapoint</code> resource or lists <code>indexes_datapoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indexes_datapoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.indexes_datapoints" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="remove_datapoints" /> | `DELETE` | <CopyableCode code="indexesId, locationsId, projectsId" /> | Remove Datapoints from an Index. |

## `DELETE` example

Deletes the specified indexes_datapoint resource.

```sql
DELETE FROM google.aiplatform.indexes_datapoints
WHERE indexesId = '{{ indexesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

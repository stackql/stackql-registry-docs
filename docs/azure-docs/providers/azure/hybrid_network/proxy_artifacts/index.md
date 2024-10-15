---
title: proxy_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - proxy_artifacts
  - hybrid_network
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

Creates, updates, deletes, gets or lists a <code>proxy_artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proxy_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.proxy_artifacts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactName, artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Get a Artifact overview information. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Lists all the available artifacts in the parent Artifact Store. |

## `SELECT` examples

Lists all the available artifacts in the parent Artifact Store.


```sql
SELECT

FROM azure.hybrid_network.proxy_artifacts
WHERE artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
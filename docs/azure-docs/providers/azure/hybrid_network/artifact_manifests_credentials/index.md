---
title: artifact_manifests_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_manifests_credentials
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

Creates, updates, deletes, gets or lists a <code>artifact_manifests_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifact_manifests_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.artifact_manifests_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="credentialType" /> | `string` | The credential type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | List credential for publishing artifacts defined in artifact manifest. |

## `SELECT` examples

List credential for publishing artifacts defined in artifact manifest.


```sql
SELECT
credentialType
FROM azure.hybrid_network.artifact_manifests_credentials
WHERE artifactManifestName = '{{ artifactManifestName }}'
AND artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
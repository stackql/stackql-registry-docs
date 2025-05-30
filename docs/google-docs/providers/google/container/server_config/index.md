---
title: server_config
hide_title: false
hide_table_of_contents: false
keywords:
  - server_config
  - container
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

Creates, updates, deletes, gets or lists a <code>server_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.container.server_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="channels" /> | `array` | List of release channel configurations. |
| <CopyableCode code="defaultClusterVersion" /> | `string` | Version of Kubernetes the service deploys by default. |
| <CopyableCode code="defaultImageType" /> | `string` | Default image type. |
| <CopyableCode code="validImageTypes" /> | `array` | List of valid image types. |
| <CopyableCode code="validMasterVersions" /> | `array` | List of valid master versions, in descending order. |
| <CopyableCode code="validNodeVersions" /> | `array` | List of valid node upgrade target versions, in descending order. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_get_server_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns configuration info about the Google Kubernetes Engine service. |

## `SELECT` examples

Returns configuration info about the Google Kubernetes Engine service.

```sql
SELECT
channels,
defaultClusterVersion,
defaultImageType,
validImageTypes,
validMasterVersions,
validNodeVersions
FROM google.container.server_config
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

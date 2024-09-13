---
title: apt_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - apt_artifacts
  - artifactregistry
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

Creates, updates, deletes, gets or lists a <code>apt_artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apt_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.apt_artifacts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Directly uploads an Apt artifact. The returned Operation will complete once the resources are uploaded. Package, Version, and File resources are created based on the imported artifact. Imported artifacts that conflict with existing resources are ignored. |

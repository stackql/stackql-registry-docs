
---
title: generic_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - generic_artifacts
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

Creates, updates, deletes or gets an <code>generic_artifact</code> resource or lists <code>generic_artifacts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>generic_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.generic_artifacts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Directly uploads a Generic artifact. The returned operation will complete once the resources are uploaded. Package, version, and file resources are created based on the uploaded artifact. Uploaded artifacts that conflict with existing resources will raise an `ALREADY_EXISTS` error. |

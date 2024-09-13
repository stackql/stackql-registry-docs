---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - vision
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

Creates, updates, deletes, gets or lists a <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vision.images" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="images_annotate" /> | `EXEC` | <CopyableCode code="" /> | Run image detection and annotation for a batch of images. |
| <CopyableCode code="images_async_batch_annotate" /> | `EXEC` | <CopyableCode code="" /> | Run asynchronous image detection and annotation for a list of images. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateImagesResponse` (results). This service will write image annotation outputs to json files in customer GCS bucket, each json file containing BatchAnnotateImagesResponse proto. |
| <CopyableCode code="projects_images_annotate" /> | `EXEC` | <CopyableCode code="projectsId" /> | Run image detection and annotation for a batch of images. |
| <CopyableCode code="projects_images_async_batch_annotate" /> | `EXEC` | <CopyableCode code="projectsId" /> | Run asynchronous image detection and annotation for a list of images. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateImagesResponse` (results). This service will write image annotation outputs to json files in customer GCS bucket, each json file containing BatchAnnotateImagesResponse proto. |
| <CopyableCode code="projects_locations_images_annotate" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Run image detection and annotation for a batch of images. |
| <CopyableCode code="projects_locations_images_async_batch_annotate" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Run asynchronous image detection and annotation for a list of images. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateImagesResponse` (results). This service will write image annotation outputs to json files in customer GCS bucket, each json file containing BatchAnnotateImagesResponse proto. |

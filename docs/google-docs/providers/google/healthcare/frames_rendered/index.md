---
title: frames_rendered
hide_title: false
hide_table_of_contents: false
keywords:
  - frames_rendered
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>frames_rendered</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>frames_rendered</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.frames_rendered" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentType" /> | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| <CopyableCode code="data" /> | `string` | The HTTP request/response body as raw binary. |
| <CopyableCode code="extensions" /> | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="retrieve_rendered" /> | `SELECT` | <CopyableCode code="datasetsId, dicomStoresId, framesId, instancesId, locationsId, projectsId, seriesId, studiesId" /> | RetrieveRenderedFrames returns instances associated with the given study, series, SOP Instance UID and frame numbers in an acceptable Rendered Media Type. See [RetrieveTransaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4). For details on the implementation of RetrieveRenderedFrames, see [Rendered resources](https://cloud.google.com/healthcare/docs/dicom#rendered_resources) in the Cloud Healthcare API conformance statement. For samples that show how to call RetrieveRenderedFrames, see [Retrieve consumer image formats](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#retrieve-consumer). |

## `SELECT` examples

RetrieveRenderedFrames returns instances associated with the given study, series, SOP Instance UID and frame numbers in an acceptable Rendered Media Type. See [RetrieveTransaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4). For details on the implementation of RetrieveRenderedFrames, see [Rendered resources](https://cloud.google.com/healthcare/docs/dicom#rendered_resources) in the Cloud Healthcare API conformance statement. For samples that show how to call RetrieveRenderedFrames, see [Retrieve consumer image formats](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#retrieve-consumer).

```sql
SELECT
contentType,
data,
extensions
FROM google.healthcare.frames_rendered
WHERE datasetsId = '{{ datasetsId }}'
AND dicomStoresId = '{{ dicomStoresId }}'
AND framesId = '{{ framesId }}'
AND instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND seriesId = '{{ seriesId }}'
AND studiesId = '{{ studiesId }}'; 
```

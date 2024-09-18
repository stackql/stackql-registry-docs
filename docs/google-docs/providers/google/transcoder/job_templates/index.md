---
title: job_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - job_templates
  - transcoder
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

Creates, updates, deletes, gets or lists a <code>job_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.transcoder.job_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the job template. Format: `projects/{project_number}/locations/{location}/jobTemplates/{job_template}` |
| <CopyableCode code="config" /> | `object` | Job configuration |
| <CopyableCode code="labels" /> | `object` | The labels associated with this job template. You can use these to organize and group your job templates. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobTemplatesId, locationsId, projectsId" /> | Returns the job template data. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists job templates in the specified region. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a job template in the specified region. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobTemplatesId, locationsId, projectsId" /> | Deletes a job template. |

## `SELECT` examples

Lists job templates in the specified region.

```sql
SELECT
name,
config,
labels
FROM google.transcoder.job_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_templates</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.transcoder.job_templates (
locationsId,
projectsId,
name,
config,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ config }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
config:
  inputs:
    - key: string
      uri: string
      preprocessingConfig:
        color:
          saturation: number
          contrast: number
          brightness: number
        denoise:
          strength: number
          tune: string
        deblock:
          strength: number
          enabled: boolean
        audio:
          lufs: number
          highBoost: boolean
          lowBoost: boolean
        crop:
          topPixels: integer
          bottomPixels: integer
          leftPixels: integer
          rightPixels: integer
        pad:
          topPixels: integer
          bottomPixels: integer
          leftPixels: integer
          rightPixels: integer
        deinterlace:
          yadif:
            mode: string
            disableSpatialInterlacing: boolean
            parity: string
            deinterlaceAllFrames: boolean
          bwdif:
            mode: string
            parity: string
            deinterlaceAllFrames: boolean
  editList:
    - key: string
      inputs:
        - type: string
      endTimeOffset: string
      startTimeOffset: string
  elementaryStreams:
    - key: string
      videoStream:
        h264:
          widthPixels: integer
          heightPixels: integer
          frameRate: number
          frameRateConversionStrategy: string
          bitrateBps: integer
          pixelFormat: string
          rateControlMode: string
          crfLevel: integer
          allowOpenGop: boolean
          gopFrameCount: integer
          gopDuration: string
          enableTwoPass: boolean
          vbvSizeBits: integer
          vbvFullnessBits: integer
          entropyCoder: string
          bPyramid: boolean
          bFrameCount: integer
          aqStrength: number
          profile: string
          tune: string
          preset: string
          sdr: {}
          hlg: {}
        h265:
          widthPixels: integer
          heightPixels: integer
          frameRate: number
          frameRateConversionStrategy: string
          bitrateBps: integer
          pixelFormat: string
          rateControlMode: string
          crfLevel: integer
          allowOpenGop: boolean
          gopFrameCount: integer
          gopDuration: string
          enableTwoPass: boolean
          vbvSizeBits: integer
          vbvFullnessBits: integer
          bPyramid: boolean
          bFrameCount: integer
          aqStrength: number
          profile: string
          tune: string
          preset: string
          sdr: {}
          hlg: {}
          hdr10: {}
        vp9:
          widthPixels: integer
          heightPixels: integer
          frameRate: number
          frameRateConversionStrategy: string
          bitrateBps: integer
          pixelFormat: string
          rateControlMode: string
          crfLevel: integer
          gopFrameCount: integer
          gopDuration: string
          profile: string
          sdr: {}
          hlg: {}
      audioStream:
        codec: string
        bitrateBps: integer
        channelCount: integer
        channelLayout:
          - type: string
        mapping:
          - atomKey: string
            inputKey: string
            inputTrack: integer
            inputChannel: integer
            outputChannel: integer
            gainDb: number
        sampleRateHertz: integer
        languageCode: string
        displayName: string
      textStream:
        codec: string
        languageCode: string
        mapping:
          - atomKey: string
            inputKey: string
            inputTrack: integer
        displayName: string
  muxStreams:
    - key: string
      fileName: string
      container: string
      elementaryStreams:
        - type: string
      segmentSettings:
        segmentDuration: string
        individualSegments: boolean
      encryptionId: string
      fmp4:
        codecTag: string
  manifests:
    - fileName: string
      type: string
      muxStreams:
        - type: string
      dash:
        segmentReferenceScheme: string
  output:
    uri: string
  adBreaks:
    - startTimeOffset: string
  pubsubDestination:
    topic: string
  spriteSheets:
    - format: string
      filePrefix: string
      spriteWidthPixels: integer
      spriteHeightPixels: integer
      columnCount: integer
      rowCount: integer
      startTimeOffset: string
      endTimeOffset: string
      totalCount: integer
      interval: string
      quality: integer
  overlays:
    - image:
        uri: string
        resolution:
          x: number
          'y': number
        alpha: number
      animations:
        - animationStatic:
            startTimeOffset: string
          animationFade:
            fadeType: string
            startTimeOffset: string
            endTimeOffset: string
          animationEnd:
            startTimeOffset: string
  encryptions:
    - id: string
      aes128: {}
      sampleAes: {}
      mpegCenc:
        scheme: string
      secretManagerKeySource:
        secretVersion: string
      drmSystems:
        widevine: {}
        fairplay: {}
        playready: {}
        clearkey: {}
labels: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.transcoder.job_templates
WHERE jobTemplatesId = '{{ jobTemplatesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

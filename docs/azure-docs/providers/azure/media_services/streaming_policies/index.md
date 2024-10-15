---
title: streaming_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_policies
  - media_services
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

Creates, updates, deletes, gets or lists a <code>streaming_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.streaming_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_streaming_policies', value: 'view', },
        { label: 'streaming_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="common_encryption_cbcs" /> | `text` | field from the `properties` object |
| <CopyableCode code="common_encryption_cenc" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_content_key_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="envelope_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="no_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="streamingPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class to specify properties of Streaming Policy |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, streamingPolicyName, subscriptionId" /> | Get the details of a Streaming Policy in the Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Streaming Policies in the account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, streamingPolicyName, subscriptionId" /> | Create a Streaming Policy in the Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, streamingPolicyName, subscriptionId" /> | Deletes a Streaming Policy in the Media Services account |

## `SELECT` examples

Lists the Streaming Policies in the account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_streaming_policies', value: 'view', },
        { label: 'streaming_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
common_encryption_cbcs,
common_encryption_cenc,
created,
default_content_key_policy_name,
envelope_encryption,
no_encryption,
resourceGroupName,
streamingPolicyName,
subscriptionId,
system_data
FROM azure.media_services.vw_streaming_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.media_services.streaming_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streaming_policies</code> resource.

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
INSERT INTO azure.media_services.streaming_policies (
accountName,
resourceGroupName,
streamingPolicyName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ streamingPolicyName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: created
          value: string
        - name: defaultContentKeyPolicyName
          value: string
        - name: envelopeEncryption
          value:
            - name: enabledProtocols
              value:
                - name: download
                  value: boolean
                - name: dash
                  value: boolean
                - name: hls
                  value: boolean
                - name: smoothStreaming
                  value: boolean
            - name: clearTracks
              value:
                - - name: trackSelections
                    value:
                      - - name: property
                          value: string
                        - name: operation
                          value: string
                        - name: value
                          value: string
            - name: contentKeys
              value:
                - name: defaultKey
                  value:
                    - name: label
                      value: string
                    - name: policyName
                      value: string
                - name: keyToTrackMappings
                  value:
                    - - name: label
                        value: string
                      - name: policyName
                        value: string
                      - name: tracks
                        value:
                          - - name: trackSelections
                              value:
                                - - name: property
                                    value: string
                                  - name: operation
                                    value: string
                                  - name: value
                                    value: string
            - name: customKeyAcquisitionUrlTemplate
              value: string
        - name: commonEncryptionCenc
          value:
            - name: clearTracks
              value:
                - - name: trackSelections
                    value:
                      - - name: property
                          value: string
                        - name: operation
                          value: string
                        - name: value
                          value: string
            - name: drm
              value:
                - name: playReady
                  value:
                    - name: customLicenseAcquisitionUrlTemplate
                      value: string
                    - name: playReadyCustomAttributes
                      value: string
                - name: widevine
                  value:
                    - name: customLicenseAcquisitionUrlTemplate
                      value: string
            - name: clearKeyEncryptionConfiguration
              value:
                - name: customKeysAcquisitionUrlTemplate
                  value: string
        - name: commonEncryptionCbcs
          value:
            - name: clearTracks
              value:
                - - name: trackSelections
                    value:
                      - - name: property
                          value: string
                        - name: operation
                          value: string
                        - name: value
                          value: string
            - name: drm
              value:
                - name: fairPlay
                  value:
                    - name: customLicenseAcquisitionUrlTemplate
                      value: string
                    - name: allowPersistentLicense
                      value: boolean
        - name: noEncryption
          value: []
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>streaming_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.streaming_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND streamingPolicyName = '{{ streamingPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

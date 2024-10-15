---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
  - test_base
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

Creates, updates, deletes, gets or lists a <code>packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.packages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packages', value: 'view', },
        { label: 'packages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="application_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="blob_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="draft_package_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="first_party_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="flighting_ring" /> | `text` | field from the `properties` object |
| <CopyableCode code="gallery_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="inplace_upgrade_os_pair" /> | `text` | field from the `properties` object |
| <CopyableCode code="intune_enrollment_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="packageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="target_os_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="tests" /> | `text` | field from the `properties` object |
| <CopyableCode code="validation_results" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of the Test Base Package. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a Test Base Package. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the packages under a Test Base Account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create or replace (overwrite/recreate, with potential downtime) a Test Base Package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a Test Base Package. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Update an existing Test Base Package. |
| <CopyableCode code="hard_delete" /> | `EXEC` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Hard Delete a Test Base Package. |
| <CopyableCode code="run_test" /> | `EXEC` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Trigger a test run on the package. |

## `SELECT` examples

Lists all the packages under a Test Base Account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packages', value: 'view', },
        { label: 'packages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
application_name,
blob_path,
draft_package_id,
first_party_apps,
flighting_ring,
gallery_apps,
inplace_upgrade_os_pair,
intune_enrollment_metadata,
is_enabled,
last_modified_time,
location,
packageName,
package_status,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
target_os_list,
testBaseAccountName,
test_types,
tests,
validation_results,
version
FROM azure_extras.test_base.vw_packages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_extras.test_base.packages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>packages</code> resource.

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
INSERT INTO azure_extras.test_base.packages (
packageName,
resourceGroupName,
subscriptionId,
testBaseAccountName,
properties,
tags,
location
)
SELECT 
'{{ packageName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ testBaseAccountName }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: applicationName
          value: string
        - name: version
          value: string
        - name: draftPackageId
          value: string
        - name: packageStatus
          value: string
        - name: isEnabled
          value: boolean
        - name: blobPath
          value: string
        - name: validationResults
          value:
            - - name: validationName
                value: string
              - name: isValid
                value: boolean
              - name: errors
                value:
                  - string
        - name: testTypes
          value:
            - []
        - name: targetOSList
          value:
            - - name: osUpdateType
                value: string
              - name: targetOSs
                value:
                  - string
              - name: insiderChannelIds
                value:
                  - string
              - name: baselineOSs
                value:
                  - string
              - name: targetOSImageIds
                value:
                  - string
        - name: inplaceUpgradeOSPair
          value:
            - name: baselineOS
              value:
                - name: osName
                  value: string
                - name: customImageId
                  value: string
                - name: customImageDisplayName
                  value: string
                - name: releaseProperties
                  value:
                    - name: releaseName
                      value: string
                    - name: buildNumber
                      value: string
                    - name: buildRevision
                      value: string
                    - name: releaseVersionDate
                      value: string
            - name: targetOS
              value: string
        - name: lastModifiedTime
          value: string
        - name: flightingRing
          value: string
        - name: firstPartyApps
          value:
            - - name: name
                value: string
              - name: architecture
                value: []
              - name: channel
                value: string
              - name: ring
                value: string
              - name: interopExecutionMode
                value: string
        - name: galleryApps
          value:
            - - name: skuId
                value: string
              - name: isConsented
                value: boolean
        - name: tests
          value:
            - - name: testType
                value: []
              - name: validationRunStatus
                value: string
              - name: validationResultId
                value: string
              - name: isActive
                value: boolean
              - name: commands
                value:
                  - - name: name
                      value: string
                    - name: action
                      value: string
                    - name: contentType
                      value: string
                    - name: content
                      value: string
                    - name: runElevated
                      value: boolean
                    - name: restartAfter
                      value: boolean
                    - name: maxRunTime
                      value: integer
                    - name: runAsInteractive
                      value: boolean
                    - name: alwaysRun
                      value: boolean
                    - name: applyUpdateBefore
                      value: boolean
                    - name: install1PAppBefore
                      value: boolean
                    - name: preUpgrade
                      value: boolean
                    - name: postUpgrade
                      value: boolean
                    - name: enrollIntuneBefore
                      value: boolean
        - name: intuneEnrollmentMetadata
          value:
            - name: appList
              value:
                - - name: appName
                    value: string
                  - name: appId
                    value: string
                  - name: expectedInstallationPath
                    value: string
            - name: credentialId
              value: string
            - name: expectedDeploymentDurationInMinute
              value: integer
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>packages</code> resource.

```sql
/*+ update */
UPDATE azure_extras.test_base.packages
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```

## `DELETE` example

Deletes the specified <code>packages</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.packages
WHERE packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```

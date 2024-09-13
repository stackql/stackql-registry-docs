---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
  - run
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

Creates, updates, deletes or gets an <code>revision</code> resource or lists <code>revisions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.run.revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The unique name of this Revision. |
| <CopyableCode code="annotations" /> | `object` | Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. |
| <CopyableCode code="conditions" /> | `array` | Output only. The Condition of this Revision, containing its readiness status, and detailed error information in case it did not reach a serving state. |
| <CopyableCode code="containers" /> | `array` | Holds the single container that defines the unit of execution for this Revision. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| <CopyableCode code="encryptionKey" /> | `string` | A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |
| <CopyableCode code="encryptionKeyRevocationAction" /> | `string` | The action to take if the encryption key is revoked. |
| <CopyableCode code="encryptionKeyShutdownDuration" /> | `string` | If encryption_key_revocation_action is SHUTDOWN, the duration before shutting down all instances. The minimum increment is 1 hour. |
| <CopyableCode code="etag" /> | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| <CopyableCode code="executionEnvironment" /> | `string` | The execution environment being used to host this Revision. |
| <CopyableCode code="expireTime" /> | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| <CopyableCode code="generation" /> | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| <CopyableCode code="labels" /> | `object` | Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels. |
| <CopyableCode code="launchStage" /> | `string` | The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA. |
| <CopyableCode code="logUri" /> | `string` | Output only. The Google Console URI to obtain logs for the Revision. |
| <CopyableCode code="maxInstanceRequestConcurrency" /> | `integer` | Sets the maximum number of requests that each serving instance can receive. |
| <CopyableCode code="nodeSelector" /> | `object` | Hardware constraints configuration. |
| <CopyableCode code="observedGeneration" /> | `string` | Output only. The generation of this Revision currently serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Service.reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="scaling" /> | `object` | Settings for revision-level scaling settings. |
| <CopyableCode code="scalingStatus" /> | `object` | Effective settings for the current revision |
| <CopyableCode code="service" /> | `string` | Output only. The name of the parent service. |
| <CopyableCode code="serviceAccount" /> | `string` | Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. |
| <CopyableCode code="serviceMesh" /> | `object` | Settings for Cloud Service Mesh. For more information see https://cloud.google.com/service-mesh/docs/overview. |
| <CopyableCode code="sessionAffinity" /> | `boolean` | Enable session affinity. |
| <CopyableCode code="timeout" /> | `string` | Max allowed time for an instance to respond to a request. |
| <CopyableCode code="uid" /> | `string` | Output only. Server assigned unique identifier for the Revision. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last-modified time. |
| <CopyableCode code="volumes" /> | `array` | A list of Volumes to make available to containers. |
| <CopyableCode code="vpcAccess" /> | `object` | VPC Access settings. For more information on sending traffic to a VPC network, visit https://cloud.google.com/run/docs/configuring/connecting-vpc. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, revisionsId, servicesId" /> | Gets information about a Revision. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists Revisions from a given Service, or from a given location. Results are sorted by creation time, descending. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, revisionsId, servicesId" /> | Deletes a Revision. |
| <CopyableCode code="export_status" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, revisionsId, revisionsId1, servicesId" /> | Read the status of an image export operation. |

## `SELECT` examples

Lists Revisions from a given Service, or from a given location. Results are sorted by creation time, descending.

```sql
SELECT
name,
annotations,
conditions,
containers,
createTime,
deleteTime,
encryptionKey,
encryptionKeyRevocationAction,
encryptionKeyShutdownDuration,
etag,
executionEnvironment,
expireTime,
generation,
labels,
launchStage,
logUri,
maxInstanceRequestConcurrency,
nodeSelector,
observedGeneration,
reconciling,
satisfiesPzs,
scaling,
scalingStatus,
service,
serviceAccount,
serviceMesh,
sessionAffinity,
timeout,
uid,
updateTime,
volumes,
vpcAccess
FROM google.run.revisions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}'; 
```

## `DELETE` example

Deletes the specified revision resource.

```sql
DELETE FROM google.run.revisions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND revisionsId = '{{ revisionsId }}'
AND servicesId = '{{ servicesId }}';
```

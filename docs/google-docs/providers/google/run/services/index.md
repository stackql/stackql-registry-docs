---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.run.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The fully qualified name of this Service. In CreateServiceRequest, this field is ignored, and instead composed from CreateServiceRequest.parent and CreateServiceRequest.service_id. Format: projects/{project}/locations/{location}/services/{service_id} |
| <CopyableCode code="description" /> | `string` | User-provided description of the Service. This field currently has a 512-character limit. |
| <CopyableCode code="annotations" /> | `object` | Optional. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run API v2 does not support annotations with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected in new resources. All system annotations in v1 now have a corresponding field in v2 Service. This field follows Kubernetes annotations' namespacing, limits, and rules. |
| <CopyableCode code="binaryAuthorization" /> | `object` | Settings for Binary Authorization feature. |
| <CopyableCode code="client" /> | `string` | Arbitrary identifier for the API client. |
| <CopyableCode code="clientVersion" /> | `string` | Arbitrary version identifier for the API client. |
| <CopyableCode code="conditions" /> | `array` | Output only. The Conditions of all other associated sub-resources. They contain additional diagnostics information in case the Service does not reach its Serving state. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time. |
| <CopyableCode code="creator" /> | `string` | Output only. Email address of the authenticated creator. |
| <CopyableCode code="customAudiences" /> | `array` | One or more custom audiences that you want this service to support. Specify each custom audience as the full URL in a string. The custom audiences are encoded in the token and used to authenticate requests. For more information, see https://cloud.google.com/run/docs/configuring/custom-audiences. |
| <CopyableCode code="defaultUriDisabled" /> | `boolean` | Optional. Disables public resolution of the default URI of this service. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The deletion time. It is only populated as a response to a Delete request. |
| <CopyableCode code="etag" /> | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| <CopyableCode code="expireTime" /> | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. |
| <CopyableCode code="generation" /> | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. Please note that unlike v1, this is an int64 value. As with most Google APIs, its JSON representation will be a `string` instead of an `integer`. |
| <CopyableCode code="ingress" /> | `string` | Optional. Provides the ingress settings for this Service. On output, returns the currently observed ingress settings, or INGRESS_TRAFFIC_UNSPECIFIED if no revision is active. |
| <CopyableCode code="labels" /> | `object` | Optional. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels. Cloud Run API v2 does not support labels with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected. All system labels in v1 now have a corresponding field in v2 Service. |
| <CopyableCode code="lastModifier" /> | `string` | Output only. Email address of the last authenticated modifier. |
| <CopyableCode code="latestCreatedRevision" /> | `string` | Output only. Name of the last created revision. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="latestReadyRevision" /> | `string` | Output only. Name of the latest revision that is serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="launchStage" /> | `string` | Optional. The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, GA is assumed. Set the launch stage to a preview stage on input to allow use of preview features in that stage. On read (or output), describes whether the resource uses preview features. For example, if ALPHA is provided as input, but only BETA and GA-level features are used, this field will be BETA on output. |
| <CopyableCode code="observedGeneration" /> | `string` | Output only. The generation of this Service currently serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. Please note that unlike v1, this is an int64 value. As with most Google APIs, its JSON representation will be a `string` instead of an `integer`. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Returns true if the Service is currently being acted upon by the system to bring it into the desired state. When a new Service is created, or an existing one is updated, Cloud Run will asynchronously perform all necessary steps to bring the Service to the desired serving state. This process is called reconciliation. While reconciliation is in process, `observed_generation`, `latest_ready_revison`, `traffic_statuses`, and `uri` will have transient values that might mismatch the intended state: Once reconciliation is over (and this field is false), there are two possible outcomes: reconciliation succeeded and the serving state matches the Service, or there was an error, and reconciliation failed. This state can be found in `terminal_condition.state`. If reconciliation succeeded, the following fields will match: `traffic` and `traffic_statuses`, `observed_generation` and `generation`, `latest_ready_revision` and `latest_created_revision`. If reconciliation failed, `traffic_statuses`, `observed_generation`, and `latest_ready_revision` will have the state of the last serving revision, or empty for newly created Services. Additional information on the failure can be found in `terminal_condition` and `conditions`. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="scaling" /> | `object` | Scaling settings applied at the service level rather than at the revision level. |
| <CopyableCode code="template" /> | `object` | RevisionTemplate describes the data a revision should have when created from a template. |
| <CopyableCode code="terminalCondition" /> | `object` | Defines a status condition for a resource. |
| <CopyableCode code="traffic" /> | `array` | Optional. Specifies how to distribute traffic over a collection of Revisions belonging to the Service. If traffic is empty or not provided, defaults to 100% traffic to the latest `Ready` Revision. |
| <CopyableCode code="trafficStatuses" /> | `array` | Output only. Detailed status information for corresponding traffic targets. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="uid" /> | `string` | Output only. Server assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last-modified time. |
| <CopyableCode code="uri" /> | `string` | Output only. The main URI in which this Service is serving traffic. |
| <CopyableCode code="urls" /> | `array` | Output only. All URLs serving traffic for this Service. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Gets information about a Service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Services. Results are sorted by creation time, descending. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Service in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Deletes a Service. This will cause the Service to stop serving traffic and will delete all revisions. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Updates a Service. |

## `SELECT` examples

Lists Services. Results are sorted by creation time, descending.

```sql
SELECT
name,
description,
annotations,
binaryAuthorization,
client,
clientVersion,
conditions,
createTime,
creator,
customAudiences,
defaultUriDisabled,
deleteTime,
etag,
expireTime,
generation,
ingress,
labels,
lastModifier,
latestCreatedRevision,
latestReadyRevision,
launchStage,
observedGeneration,
reconciling,
satisfiesPzs,
scaling,
template,
terminalCondition,
traffic,
trafficStatuses,
uid,
updateTime,
uri,
urls
FROM google.run.services
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO google.run.services (
locationsId,
projectsId,
name,
description,
labels,
annotations,
client,
clientVersion,
ingress,
launchStage,
binaryAuthorization,
template,
traffic,
scaling,
defaultUriDisabled,
customAudiences
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}',
'{{ annotations }}',
'{{ client }}',
'{{ clientVersion }}',
'{{ ingress }}',
'{{ launchStage }}',
'{{ binaryAuthorization }}',
'{{ template }}',
'{{ traffic }}',
'{{ scaling }}',
{{ defaultUriDisabled }},
'{{ customAudiences }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: uid
      value: string
    - name: generation
      value: string
    - name: labels
      value: object
    - name: annotations
      value: object
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: deleteTime
      value: string
    - name: expireTime
      value: string
    - name: creator
      value: string
    - name: lastModifier
      value: string
    - name: client
      value: string
    - name: clientVersion
      value: string
    - name: ingress
      value: string
    - name: launchStage
      value: string
    - name: binaryAuthorization
      value:
        - name: useDefault
          value: boolean
        - name: policy
          value: string
        - name: breakglassJustification
          value: string
    - name: template
      value:
        - name: revision
          value: string
        - name: labels
          value: object
        - name: annotations
          value: object
        - name: scaling
          value:
            - name: minInstanceCount
              value: integer
            - name: maxInstanceCount
              value: integer
        - name: vpcAccess
          value:
            - name: connector
              value: string
            - name: egress
              value: string
            - name: networkInterfaces
              value:
                - - name: network
                    value: string
                  - name: subnetwork
                    value: string
                  - name: tags
                    value:
                      - string
        - name: timeout
          value: string
        - name: serviceAccount
          value: string
        - name: containers
          value:
            - - name: name
                value: string
              - name: image
                value: string
              - name: command
                value:
                  - string
              - name: args
                value:
                  - string
              - name: env
                value:
                  - - name: name
                      value: string
                    - name: value
                      value: string
                    - name: valueSource
                      value:
                        - name: secretKeyRef
                          value:
                            - name: secret
                              value: string
                            - name: version
                              value: string
              - name: resources
                value:
                  - name: limits
                    value: object
                  - name: cpuIdle
                    value: boolean
                  - name: startupCpuBoost
                    value: boolean
              - name: ports
                value:
                  - - name: name
                      value: string
                    - name: containerPort
                      value: integer
              - name: volumeMounts
                value:
                  - - name: name
                      value: string
                    - name: mountPath
                      value: string
              - name: workingDir
                value: string
              - name: livenessProbe
                value:
                  - name: initialDelaySeconds
                    value: integer
                  - name: timeoutSeconds
                    value: integer
                  - name: periodSeconds
                    value: integer
                  - name: failureThreshold
                    value: integer
                  - name: httpGet
                    value:
                      - name: path
                        value: string
                      - name: httpHeaders
                        value:
                          - - name: name
                              value: string
                            - name: value
                              value: string
                      - name: port
                        value: integer
                  - name: tcpSocket
                    value:
                      - name: port
                        value: integer
                  - name: grpc
                    value:
                      - name: port
                        value: integer
                      - name: service
                        value: string
              - name: dependsOn
                value:
                  - string
        - name: volumes
          value:
            - - name: name
                value: string
              - name: secret
                value:
                  - name: secret
                    value: string
                  - name: items
                    value:
                      - - name: path
                          value: string
                        - name: version
                          value: string
                        - name: mode
                          value: integer
                  - name: defaultMode
                    value: integer
              - name: cloudSqlInstance
                value:
                  - name: instances
                    value:
                      - string
              - name: emptyDir
                value:
                  - name: medium
                    value: string
                  - name: sizeLimit
                    value: string
              - name: nfs
                value:
                  - name: server
                    value: string
                  - name: path
                    value: string
                  - name: readOnly
                    value: boolean
              - name: gcs
                value:
                  - name: bucket
                    value: string
                  - name: readOnly
                    value: boolean
        - name: executionEnvironment
          value: string
        - name: encryptionKey
          value: string
        - name: maxInstanceRequestConcurrency
          value: integer
        - name: serviceMesh
          value:
            - name: mesh
              value: string
        - name: sessionAffinity
          value: boolean
        - name: healthCheckDisabled
          value: boolean
        - name: nodeSelector
          value:
            - name: accelerator
              value: string
    - name: traffic
      value:
        - - name: type
            value: string
          - name: revision
            value: string
          - name: percent
            value: integer
          - name: tag
            value: string
    - name: scaling
      value:
        - name: minInstanceCount
          value: integer
        - name: scalingMode
          value: string
    - name: defaultUriDisabled
      value: boolean
    - name: urls
      value:
        - string
    - name: customAudiences
      value:
        - string
    - name: observedGeneration
      value: string
    - name: terminalCondition
      value:
        - name: type
          value: string
        - name: state
          value: string
        - name: message
          value: string
        - name: lastTransitionTime
          value: string
        - name: severity
          value: string
        - name: reason
          value: string
        - name: revisionReason
          value: string
        - name: executionReason
          value: string
    - name: conditions
      value:
        - - name: type
            value: string
          - name: state
            value: string
          - name: message
            value: string
          - name: lastTransitionTime
            value: string
          - name: severity
            value: string
          - name: reason
            value: string
          - name: revisionReason
            value: string
          - name: executionReason
            value: string
    - name: latestReadyRevision
      value: string
    - name: latestCreatedRevision
      value: string
    - name: trafficStatuses
      value:
        - - name: type
            value: string
          - name: revision
            value: string
          - name: percent
            value: integer
          - name: tag
            value: string
          - name: uri
            value: string
    - name: uri
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: reconciling
      value: boolean
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE google.run.services
SET 
name = '{{ name }}',
description = '{{ description }}',
labels = '{{ labels }}',
annotations = '{{ annotations }}',
client = '{{ client }}',
clientVersion = '{{ clientVersion }}',
ingress = '{{ ingress }}',
launchStage = '{{ launchStage }}',
binaryAuthorization = '{{ binaryAuthorization }}',
template = '{{ template }}',
traffic = '{{ traffic }}',
scaling = '{{ scaling }}',
defaultUriDisabled = true|false,
customAudiences = '{{ customAudiences }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM google.run.services
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

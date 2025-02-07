---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - monitoring
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name for this Service. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]  |
| <CopyableCode code="appEngine" /> | `object` | App Engine service. Learn more at https://cloud.google.com/appengine. |
| <CopyableCode code="basicService" /> | `object` | A well-known service type, defined by its service type and service labels. Documentation and examples here (https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli). |
| <CopyableCode code="cloudEndpoints" /> | `object` | Cloud Endpoints service. Learn more at https://cloud.google.com/endpoints. |
| <CopyableCode code="cloudRun" /> | `object` | Cloud Run service. Learn more at https://cloud.google.com/run. |
| <CopyableCode code="clusterIstio" /> | `object` | Istio service scoped to a single Kubernetes cluster. Learn more at https://istio.io. Clusters running OSS Istio will have their services ingested as this type. |
| <CopyableCode code="custom" /> | `object` | Use a custom service to designate a service that you want to monitor when none of the other service types (like App Engine, Cloud Run, or a GKE type) matches your intended service. |
| <CopyableCode code="displayName" /> | `string` | Name used for UI elements listing this Service. |
| <CopyableCode code="gkeNamespace" /> | `object` | GKE Namespace. The field names correspond to the resource metadata labels on monitored resources that fall under a namespace (for example, k8s_container or k8s_pod). |
| <CopyableCode code="gkeService" /> | `object` | GKE Service. The "service" here represents a Kubernetes service object (https://kubernetes.io/docs/concepts/services-networking/service). The field names correspond to the resource labels on k8s_service monitored resources (https://cloud.google.com/monitoring/api/resources#tag_k8s_service). |
| <CopyableCode code="gkeWorkload" /> | `object` | A GKE Workload (Deployment, StatefulSet, etc). The field names correspond to the metadata labels on monitored resources that fall under a workload (for example, k8s_container or k8s_pod). |
| <CopyableCode code="istioCanonicalService" /> | `object` | Canonical service scoped to an Istio mesh. Anthos clusters running ASM >= 1.6.8 will have their services ingested as this type. |
| <CopyableCode code="meshIstio" /> | `object` | Istio service scoped to an Istio mesh. Anthos clusters running ASM < 1.6.8 will have their services ingested as this type. |
| <CopyableCode code="telemetry" /> | `object` | Configuration for how to query telemetry on a Service. |
| <CopyableCode code="userLabels" /> | `object` | Labels which have been used to annotate the service. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="services_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | List Services for this Metrics Scope. |
| <CopyableCode code="services_create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Create a Service. |

## `SELECT` examples

List Services for this Metrics Scope.

```sql
SELECT
name,
appEngine,
basicService,
cloudEndpoints,
cloudRun,
clusterIstio,
custom,
displayName,
gkeNamespace,
gkeService,
gkeWorkload,
istioCanonicalService,
meshIstio,
telemetry,
userLabels
FROM google.monitoring.services
WHERE parent = '{{ parent }}'
AND parentType = '{{ parentType }}';
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
INSERT INTO google.monitoring.services (
parent,
parentType,
name,
displayName,
custom,
appEngine,
cloudEndpoints,
clusterIstio,
meshIstio,
istioCanonicalService,
cloudRun,
gkeNamespace,
gkeWorkload,
gkeService,
basicService,
telemetry,
userLabels
)
SELECT 
'{{ parent }}',
'{{ parentType }}',
'{{ name }}',
'{{ displayName }}',
'{{ custom }}',
'{{ appEngine }}',
'{{ cloudEndpoints }}',
'{{ clusterIstio }}',
'{{ meshIstio }}',
'{{ istioCanonicalService }}',
'{{ cloudRun }}',
'{{ gkeNamespace }}',
'{{ gkeWorkload }}',
'{{ gkeService }}',
'{{ basicService }}',
'{{ telemetry }}',
'{{ userLabels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: custom
      value: []
    - name: appEngine
      value:
        - name: moduleId
          value: string
    - name: cloudEndpoints
      value:
        - name: service
          value: string
    - name: clusterIstio
      value:
        - name: location
          value: string
        - name: clusterName
          value: string
        - name: serviceNamespace
          value: string
        - name: serviceName
          value: string
    - name: meshIstio
      value:
        - name: meshUid
          value: string
        - name: serviceNamespace
          value: string
        - name: serviceName
          value: string
    - name: istioCanonicalService
      value:
        - name: meshUid
          value: string
        - name: canonicalServiceNamespace
          value: string
        - name: canonicalService
          value: string
    - name: cloudRun
      value:
        - name: serviceName
          value: string
        - name: location
          value: string
    - name: gkeNamespace
      value:
        - name: projectId
          value: string
        - name: location
          value: string
        - name: clusterName
          value: string
        - name: namespaceName
          value: string
    - name: gkeWorkload
      value:
        - name: projectId
          value: string
        - name: location
          value: string
        - name: clusterName
          value: string
        - name: namespaceName
          value: string
        - name: topLevelControllerType
          value: string
        - name: topLevelControllerName
          value: string
    - name: gkeService
      value:
        - name: projectId
          value: string
        - name: location
          value: string
        - name: clusterName
          value: string
        - name: namespaceName
          value: string
        - name: serviceName
          value: string
    - name: basicService
      value:
        - name: serviceType
          value: string
        - name: serviceLabels
          value: object
    - name: telemetry
      value:
        - name: resourceName
          value: string
    - name: userLabels
      value: object

```
</TabItem>
</Tabs>

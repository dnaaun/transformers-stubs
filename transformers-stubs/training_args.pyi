from typing import Optional

def default_logdir() -> str: ...

class TrainingArguments:
    output_dir: str = ...
    overwrite_output_dir: bool = ...
    do_train: bool = ...
    do_eval: bool = ...
    do_predict: bool = ...
    evaluate_during_training: bool = ...
    per_device_train_batch_size: int = ...
    per_device_eval_batch_size: int = ...
    per_gpu_train_batch_size: Optional[int] = ...
    per_gpu_eval_batch_size: Optional[int] = ...
    gradient_accumulation_steps: int = ...
    learning_rate: float = ...
    weight_decay: float = ...
    adam_beta1: float = ...
    adam_beta2: float = ...
    adam_epsilon: float = ...
    max_grad_norm: float = ...
    num_train_epochs: float = ...
    max_steps: int = ...
    warmup_steps: int = ...
    logging_dir: Optional[str] = ...
    logging_first_step: bool = ...
    logging_steps: int = ...
    save_steps: int = ...
    save_total_limit: Optional[int] = ...
    no_cuda: bool = ...
    seed: int = ...
    fp16: bool = ...
    fp16_opt_level: str = ...
    local_rank: int = ...
    tpu_num_cores: Optional[int] = ...
    tpu_metrics_debug: bool = ...
    debug: bool = ...
    dataloader_drop_last: bool = ...
    eval_steps: int = ...
    past_index: int = ...
    def __init__(
        self,
        output_dir: str = ...,
        overwrite_output_dir: bool = ...,
        do_train: bool = ...,
        do_eval: bool = ...,
        do_predict: bool = ...,
        evaluate_during_training: bool = ...,
        per_device_train_batch_size: int = ...,
        per_device_eval_batch_size: int = ...,
        per_gpu_train_batch_size: Optional[int] = ...,
        per_gpu_eval_batch_size: Optional[int] = ...,
        gradient_accumulation_steps: int = ...,
        learning_rate: float = ...,
        weight_decay: float = ...,
        adam_beta1: float = ...,
        adam_beta2: float = ...,
        adam_epsilon: float = ...,
        max_grad_norm: float = ...,
        num_train_epochs: float = ...,
        max_steps: int = ...,
        warmup_steps: int = ...,
        logging_dir: Optional[str] = ...,
        logging_first_step: bool = ...,
        logging_steps: int = ...,
        save_steps: int = ...,
        save_total_limit: Optional[int] = ...,
        no_cuda: bool = ...,
        seed: int = ...,
        fp16: bool = ...,
        fp16_opt_level: str = ...,
        local_rank: int = ...,
        tpu_num_cores: Optional[int] = ...,
        tpu_metrics_debug: bool = ...,
        debug: bool = ...,
        dataloader_drop_last: bool = ...,
        eval_steps: int = ...,
        past_index: int = ...,
    ) -> None:
        ...,

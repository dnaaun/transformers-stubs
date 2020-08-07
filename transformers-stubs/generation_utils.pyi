class GenerationMixin:
    #    def prepare_inputs_for_generation(self, input_ids, **kwargs):
    #        return {"input_ids": input_ids}
    #    def adjust_logits_during_generation(self, logits, **kwargs):
    #        return logits
    #    def enforce_repetition_penalty_(
    #        self, lprobs, batch_size, num_beams, prev_output_tokens, repetition_penalty
    #    ) -> None: ...
    #    def postprocess_next_token_scores(
    #        self,
    #        scores,
    #        input_ids,
    #        no_repeat_ngram_size,
    #        bad_words_ids,
    #        cur_len,
    #        min_length,
    #        max_length,
    #        eos_token_id,
    #        repetition_penalty,
    #        batch_size,
    #        num_beams,
    #    ) : ...
    #    @torch.no_grad()
    #    def generate(
    #        self,
    #        input_ids: Optional[torch.LongTensor] = None,
    #        max_length: Optional[int] = None,
    #        min_length: Optional[int] = None,
    #        do_sample: Optional[bool] = None,
    #        early_stopping: Optional[bool] = None,
    #        num_beams: Optional[int] = None,
    #        temperature: Optional[float] = None,
    #        top_k: Optional[int] = None,
    #        top_p: Optional[float] = None,
    #        repetition_penalty: Optional[float] = None,
    #        bad_words_ids: Optional[Iterable[int]] = None,
    #        bos_token_id: Optional[int] = None,
    #        pad_token_id: Optional[int] = None,
    #        eos_token_id: Optional[int] = None,
    #        length_penalty: Optional[float] = None,
    #        no_repeat_ngram_size: Optional[int] = None,
    #        num_return_sequences: Optional[int] = None,
    #        attention_mask: Optional[torch.LongTensor] = None,
    #        decoder_start_token_id: Optional[int] = None,
    #        use_cache: Optional[bool] = None,
    #        **model_specific_kwargs,
    #    ) -> torch.LongTensor: ...
    pass
